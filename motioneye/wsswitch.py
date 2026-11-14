# Copyright (c) 2020 Vlsarro
# Copyright (c) 2013 Calin Crisan
# This file is part of motionEye.
#
# motionEye is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

import logging
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gettext import gettext as _  # noqa: TC004

from tornado.ioloop import IOLoop

from motioneye import config, motionctl, utils

# the motion detection state set for each camera by the working schedule: it is
# only enforced again when the schedule changes, so that a manual change lasts
_ws_state: dict[int, bool] = {}


def _start_check_ws() -> None:
    IOLoop.current().spawn_callback(_check_ws)


def clear_cache() -> None:
    _ws_state.clear()


def start() -> None:
    IOLoop.current().call_later(1, _start_check_ws)
    logging.info(_('wsswitch komenciĝis'))


def _day_range(ws_day: str) -> tuple[int, int] | None:
    """The minutes of the day a working schedule day starts and ends at, or None
    when the day is disabled or invalid."""
    parts = ws_day.split('-')
    if len(parts) != 2:
        return None  # invalid ws

    if not parts[0] or not parts[1]:
        return None  # ws disabled for this day

    _from = parts[0].split(':')
    to = parts[1].split(':')
    if len(_from) != 2 or len(to) != 2:
        return None  # invalid ws

    try:
        return int(_from[0]) * 60 + int(_from[1]), int(to[0]) * 60 + int(to[1])

    except ValueError:
        return None  # invalid ws


def _during_working_schedule(now, working_schedule) -> bool:
    parts = working_schedule.split('|')
    if len(parts) < 7:
        return False  # invalid ws

    minute = now.hour * 60 + now.minute
    today = _day_range(parts[now.weekday()])
    if today:
        start, end = today
        if start <= end:
            if start <= minute <= end:
                return True

        elif minute >= start:  # e.g. 22:00-06:00, which goes on the next day
            return True

    # the part after midnight of a day that goes on the next day
    yesterday = _day_range(parts[(now.weekday() - 1) % 7])
    if yesterday:
        start, end = yesterday
        if start > end and minute <= end:
            return True

    return False


async def _switch_motion_detection_status(
    camera_id,
    must_be_enabled,
    working_schedule_type,
    motion_detection_resp: utils.GetMotionDetectionResult,
) -> str | None:
    if motion_detection_resp.error:  # could not detect current status
        logging.warning(
            f'skipping motion detection status update for camera with id {camera_id}: {motion_detection_resp.error}'
        )

        return motion_detection_resp.error

    if motion_detection_resp.enabled and not must_be_enabled:
        logging.debug(
            f'must disable motion detection for camera with id {camera_id} ({working_schedule_type} working schedule)'
        )

        return await motionctl.set_motion_detection(camera_id, 'pause')

    if not motion_detection_resp.enabled and must_be_enabled:
        logging.debug(
            f'must enable motion detection for camera with id {camera_id} ({working_schedule_type} working schedule)'
        )

        return await motionctl.set_motion_detection(camera_id, 'start')

    return None


async def _check_ws() -> None:
    # schedule the next call
    IOLoop.current().call_later(10, _start_check_ws)

    if not motionctl.running():
        return

    now = datetime.now()
    for camera_id in config.get_camera_ids():
        camera_config = config.get_camera(camera_id)
        if not utils.is_local_motion_camera(camera_config):
            continue

        working_schedule = camera_config.get('@working_schedule')
        motion_detection = camera_config.get('@motion_detection')
        working_schedule_type = camera_config.get('@working_schedule_type') or 'outside'

        if (
            not working_schedule
        ):  # working schedule disabled, motion detection left untouched
            _ws_state.pop(camera_id, None)
            continue

        if not motion_detection:  # motion detection explicitly disabled
            _ws_state.pop(camera_id, None)
            continue

        now_during = _during_working_schedule(now, working_schedule)
        must_be_enabled = (now_during and working_schedule_type == 'during') or (
            not now_during and working_schedule_type == 'outside'
        )

        if _ws_state.get(camera_id) == must_be_enabled:
            continue  # set already, or changed manually since

        motion_detection_resp = await motionctl.get_motion_detection(camera_id)
        error = await _switch_motion_detection_status(
            camera_id, must_be_enabled, working_schedule_type, motion_detection_resp
        )
        if not error:  # otherwise tried again next time
            _ws_state[camera_id] = must_be_enabled
