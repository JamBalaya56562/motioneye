# Open unlabelled issues, proposal

518 open issues (#2907 to #122), classified by 6 agents on 2026-11-07 from the body and the last 3 comments. Nothing applied yet.

Sample check: 40 random issues judged without seeing the proposal: 25 of 25 high confidence agree, 10 of 15 low confidence agree. The check was made by the same model, so it is not an independent review.

`resolved?` is an agent's hint that a comment says it was solved. It is unverified, and nothing gets closed from it.

| Label | All | Low confidence |
|---|---:|---:|
| `bug` | 12 | 4 |
| `external bug` | 8 | 7 |
| `feature` | 72 | 16 |
| `enhancement` | 44 | 21 |
| `documentation` | 3 | 2 |
| `CI/CD` | 3 | 3 |
| `invalid` | 1 | 1 |
| `troubleshooting` | 195 | 63 |
| `question` | 180 | 41 |

## `bug` (12, low 4)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #2714 | low | Sunny days trigger motion | A member confirms the working schedule has an issue, though the light-change triggering itself is a known Motion limitation. |
| #2541 | low | Changing movies recording mode from "Motion Triggered" to "Continuous | A collaborator acknowledges the UI logic forces this capture mode and conflicts with workarounds; enhancement is nearly as good. |
| #1317 | low | Motion detection doesn't work when continus recording mode is enable | A collaborator reproduced constant motion detection under continuous recording, but no faulty code or fix is named. |
| #1092 resolved? | low | Stream in admin mode | Admin stream broke with Motion 4.2; a maintainer links the motionEye release that adds support for it. |
| #2578 | high | First cleanup call scheduled earlier instead of later | The report pinpoints a min versus max mistake at a specific line of cleanup.py. |
| #2504 resolved? | high | Movies not recorded | Choosing another codec fixes missing movies, and a member says motionEye's default must be changed. |
| #1449 | high | Chrome issue but not Safari or Firefox | Live view fails on Chrome 76 only, the decided Chrome case from #1401. |
| #1443 resolved? | high | Camera not displaying on MotionEyeOS | Camera not displayed, tied to the Chrome change in #1401 by a comment, and updating resolved it for a commenter. |
| #1419 resolved? | high | Camera not showing in :8765 | Camera missing in the UI but fine on the stream port; comments tie it to Chrome and Firefox works, as in #1401. |
| #790 | high | Google Chrome - flickering scrollbar | The report pinpoints a CSS margin rule behind the flicker and the maintainer acknowledges the problem. |
| #679 | high | Fullscreen not working when fit frames = on and layour rows > 1 | The maintainer confirms this as a known bug. |
| #289 resolved? | high | Token Revoked | Maintainer found upload service bugs on changing settings and links a fixing commit. |

## `external bug` (8, low 7)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #2776 | low | Recent software upgrade lead to corrupted preview images | Corrupted previews are attributed to a libmicrohttpd bug, same as #2623; motionEye dev has a workaround, so bug is nearly as good. |
| #2623 resolved? | low | Video flickers FIXED | A collaborator names libmicrohttpd as the fix target by downgrade and says 0.43 has a workaround, so bug is nearly as good. |
| #1304 resolved? | low | Error on playback iOS | Same playback failure as #1206, tied to Motion's output at 100% quality; lowering quality worked for a commenter. |
| #1206 resolved? | low | Error: Media decode error or unsupported media features | A collaborator ties it to Motion's h264 output at 100% quality via #1641, and a commenter confirms the match. |
| #1057 | low | Captured Before not working as expected? | A contributor read the Motion source and found emulate motion ignores pre-capture, which needs the Motion developers. |
| #419 | low | upgrading motioneye gives following error | Harmless pip compile error from a Jinja2 file using async syntax under Python 2; nothing in motionEye. |
| #330 | low | no smoothly video recording | Unsmooth recorded video; a contributor links the playback speed issue to a known Motion defect being fixed there. |
| #340 | high | Frame timing is off in all videos saved by Motioneye on raspberry pi 3 | Wrong video timing referred to the Motion project by the maintainer; reporter filed an issue there. |

## `feature` (72, low 16)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1519 | low | Enhancement Request: Support h264_mmal as the preferred RTSP decoder | Asks for a new option exposing a hardware RTSP decoder choice; enhancement would be about as good. |
| #1440 resolved? | low | Add temp overlay or feedback | Asks for a temperature overlay; a cron workaround from a contributor worked, so question is also plausible. |
| #1354 | low | RFC: Loop recording idea | Proposes loop recording as a new storage retention mode, same idea as #1328, with some UI rearranging. |
| #1328 | low | Enhancement: local loop recording | Requests size-based loop recording as a new retention mode, same idea as #1354. |
| #1223 | low | URL to enable / disable Motion notifications ? | Asks for a URL to toggle notifications; a commenter says motionEye has no such function. |
| #1125 | low | Support for 1 wire in MotionEyeOs / Buildroot | Requests 1-wire sensor support, though it is mainly aimed at motionEyeOS. |
| #1054 | low | Activity Log | Asks for an activity log view in the client, which does not exist; phrased partly as a question. |
| #926 | low | feature request: Add an invert mask option | Requests a new invert option for the existing motion mask. |
| #921 | low | Question: HTTP API Available | Asks for an HTTP API to run scripts; comments treat it as a wanted feature related to #972. |
| #772 | low | Save image when motion is on the display center. | Unanswered request to save images only when motion is at the centre, phrased partly as a question. |
| #338 | low | email content / notification on connection camera lost | Part how-to on email content, answered, and part still open request for an email when a camera connection is lost. |
| #315 | low | Provide ffplay | Asks to include ffplay in the prebuilt package, with no answer; could also be a packaging matter. |
| #287 | low | No Timelapse movie | Asks for real timelapse movies; a commenter says it does not exist, so it reads as a request though phrased as a question. |
| #271 | low | comands for actions - question | Asks for a terminal snapshot or video command; maintainer says not possible yet, so the need stands as a request. |
| #190 | low | feature-request: overlay image for active motion-detection | Requests an overlay showing detection is active; a commenter notes a related frame colour exists only for recording. |
| #165 | low | Support HEAD HTTP request method | Requests HEAD support; maintainer added it partly and proper responses per URI remain open. |
| #2874 | high | Request to merge the motioneye. eo library | Requests merging a fork to gain secondary stream recording and multilingual support, with no reply. |
| #2857 | high | Ability to crop image | Unanswered request for a new image cropping capability. |
| #2854 | high | Encryption on zip archive | Unanswered request for password-protected zip archives before sending media. |
| #2614 | high | Matter Support | Requests support for the Matter standard, a new capability. |
| #2592 | high | "Working Schedule" - Possible to add external gating signal? | Unanswered request for an external signal to gate motion detection. |
| #1850 | high | Option to send Google Drive link to video via email | Asks for a new option to put Google Drive links in notification emails. |
| #1846 | high | Feature requests: [1]Add GUI view that will show output for [2]custom | Requests a new GUI view for custom script output and script scheduling. |
| #1518 | high | Implement HomeKit | Asks for new HomeKit integration. |
| #1485 | high | Upload files to minio | Asks for a new MinIO upload destination. |
| #1465 | high | Adding connector to OpenCV: Feasible ? | Proposes a new OpenCV connector. |
| #1375 | high | Idea: add rsync together with ftp option | Proposes rsync as a new upload option. |
| #1315 | high | Feature request: Add option to working schedule - to notify of motion | Requests a new schedule for motion notifications. |
| #1312 | high | Add Bearer token Autorization | Requests Bearer token authentication for cameras, which is not supported. |
| #1290 | high | Add user type request to JSON Backend | Requests new JSON backend requests for a client app. |
| #1289 | high | cifs-utils in docker | Requests SMB support in the Docker image; still only discussed. |
| #1287 | high | [feature request] show images/video base on time range | Requests a new media view filtered by time range across cameras. |
| #1254 | high | SSL for streaming | Requests SSL stream configuration controlled from motionEye. |
| #1244 | high | Feature Request: Add robots.txt to static site files | Requests adding a robots.txt to the static files. |
| #1242 | high | feature request: Provide an option to change user-agent | Requests a new option to change the web hook user agent. |
| #1189 | high | Home Mode | Requests a new Home Mode that disables detection temporarily without losing settings. |
| #1158 | high | lastmovie.mp4? | Requests a new link and URL to the latest movie. |
| #1116 | high | FeatureRequest Video SpeedPlay | Requests a new fast playback mode for videos. |
| #1107 | high | Specify Separate Port for Embed URL | Requests a separate port for the embed URL, which does not exist today. |
| #1074 | high | Delete oldest media files before drive is full | Requests automatic deletion of oldest media before the disk fills, same request as #978. |
| #1058 | high | Feature Request: Movie / Picture Counts in the "Banner" | Requests picture and movie counts in the camera overlay. |
| #1040 | high | Feature request: Delete locally after successful upload te remote serv | Requests a new option to delete local files after a successful upload. |
| #1020 | high | [Feature request] Multi select in movies browser | Requests multi-selection in the movies browser. |
| #978 | high | feature request:Prevent disk filling | Requests keeping a minimum of free disk space; the maintainer plans it, same request as #1074. |
| #972 | high | When will there be an API? | Requests an API; the maintainer has no plans but would accept PRs. |
| #884 | high | Option to add a favicon | Requests a customisable favicon. |
| #850 | high | [Feature Request] Support for multiple views | Request for a new capability to group cameras into separate views. |
| #825 | high | Feature : Users and logs | Request for multiple users and a login log. |
| #808 | high | Add option to create blank .nomedia file for Google Drive uploads | Requests a new option to add a .nomedia file to Google Drive uploads; only a script workaround was offered. |
| #789 | high | feature request: Auto-generate animated GIFs | Request for auto-generated animated GIF previews. |
| #788 | high | feature request: motioneye as brightness sensor for homeautomation | Request for a brightness value output for home automation. |
| #778 | high | Integrate with free machine learning based image analysis to reduce fa | Request to integrate machine learning image analysis to filter false positives. |
| #773 | high | Feature Request - Auto create timelapse movies | Request for automatically created timelapse movies. |
| #715 | high | Add notification when a remote user connects to motioneye | Request for a notification when a remote user connects. |
| #698 | high | Feature request: Add 'During Daylight' | Request for a new daylight-based schedule option. |
| #562 | high | Video preview / animated recording video | Requests animated hover previews of recordings; no answer. |
| #538 | high | Pixel change graph over time | Requests a graph of pixel changes over time; maintainer says Motion does not allow it. |
| #455 | high | Cycling the videos of the cameras (full screen) - one per time | Requests automatic full-screen camera cycling; only a browser extension workaround offered. |
| #446 | high | MQTT (or other) Support? | Requests MQTT event publishing. |
| #413 | high | Overwrite option - uploaded files | Requests an option to overwrite uploaded files. |
| #388 | high | Hot Button | Requests one button to turn off motion on all cameras; maintainer says it does not exist yet. |
| #302 | high | Feature Request: File overwrite or delete when near full | Requests automatic overwrite or deletion when disk is nearly full, or storage alerts. |
| #279 | high | Feature request: download all button | Requests a download all button. |
| #277 | high | Feature request: choose output_picture options | Requests a choice of output picture options. |
| #273 | high | Feature request: automated (webhook) recording on/off | Requests webhook control to turn recording on and off. |
| #251 | high | de/activate motion detection by Script - not start/stop service | Asks for scriptable toggling of detection; the maintainer says the schedule logic prevents it. |
| #235 | high | External motion trigger | Requests an external HTTP or file motion trigger. |
| #203 | high | Feature requests/ideas: MotionEye activation by leaving home (using sm | Requests activation based on phone presence; users share scripts but it is not built in. |
| #200 | high | Feature request: Automatically delete older motion files in Google Dri | Requests automatic deletion of old files on Google Drive; only external workarounds offered. |
| #179 | high | Save a cropped image of the selected motion area ! | Requests saving a cropped image of the motion area. |
| #142 | high | Using Motioneye for a while, what I miss | Requests scheduled snapshots or a heartbeat to show the system is alive. |
| #122 | high | Network camera PTZ control | Requests PTZ controls for network cameras; only script workarounds shared. |

## `enhancement` (44, low 21)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #2879 | low | [feature request] Turn off preview generation option | Requests an option to switch off the existing thumbnail generation; could also count as a new feature. |
| #2826 | low | Make stream template editable / change to fullsize | Wants embeddable streams to fit their container; a collaborator says the stream comes from Motion and points to the Embed URL, which does not suit the reporter. |
| #2678 | low | Cant deactivate Authentication for Streaming | The reporter narrowed it to the Embed URL still requiring login and asks for the option there; no maintainer reply. |
| #1527 | low | [Feature Request] Multiple frames shown in the video thumbnails | Asks to improve existing video thumbnails with multiple frames; feature would be about as good. |
| #1466 | low | Feature Request - allow one motion daemon per camera | Asks to change how motion processes are run to one per camera; feature would be about as good. |
| #1359 | low | Minor question about "Still images": "Capture mode"=manual should impl | Suggests a manual snapshot switch should follow the capture mode; could also be read as a question. |
| #1353 | low | Question on video streaming frame rate vs device frame rate | Unanswered question that suggests limiting or warning about streaming frame rate in the existing UI. |
| #1137 | low | Snapshot URL token persistance | Asks if the snapshot token persists and requests it follow the streaming authentication settings. |
| #1076 | low | Please Add Mosquitto Client to the Docker Image | Asks to add the Mosquitto client to the existing Docker image, same request as #877. |
| #1013 + dup | low | Thumb | Wants thumbnails to show the motion; a comment calls it a duplicate request of #814. |
| #877 | low | Package mosquitto-clients missing in Docker | Asks to add the mosquitto client package to the Docker image, which a collaborator agrees to; same as #1076. |
| #771 | low | Can't modify sliders from mobile (android chrome) browser - makes it h | Asks to make sliders usable on mobile; the maintainer notes the UI is not mobile friendly and a redesign is planned. |
| #742 | low | Purge files based on disk usage | Asks to extend file purging, now age based, to work on disk usage. |
| #708 | low | Not all videos uploaded | Lost uploads on a slow link; maintainers state no retry mechanism exists and discuss adding one. |
| #676 | low | FPS throttling (stream_motion on) is not affecting preview stream to m | Asks to generate settings that lower frame rate when idle; the reporter also suspects a wrong config value, unconfirmed. |
| #592 | low | limit number of images during event - FTP upload | Asks to limit the rate of images per motion event for FTP upload. |
| #445 | low | Delay between email notifications | Wants a delay between notification emails; only a custom script workaround was offered, so it could also be a how-to. |
| #258 | low | Changing IP Address | Asks to include the device IP address in existing alerts; could also count as a feature. |
| #232 | low | Selective bulk delete. | Asks for selective checkbox deletion on top of the existing delete options; same request as the other bulk delete issue. |
| #195 | low | Feature request: wait for partition to be mounted on boot | Asks that startup wait for the storage mount, and the reporter identifies the existing device check as insufficient; could be read as a defect. |
| #184 | low | feature-request: bulk delete | Delete-all button exists, as the reporter found, but checkboxes for selective deletion are still wanted. |
| #2775 | high | Improve translation strings using placeholders | Asks to improve translatable strings by using placeholders the code already supports. |
| #2665 | high | Frame Change Threshold 0.1% is not enough | Asks for a finer frame change threshold; a collaborator agrees the current limit is too coarse for high resolutions. |
| #1816 | high | Delete files older than 1 hour | Asks to extend the existing preserve-pictures setting to periods shorter than a day. |
| #1712 | high | Working schedule | Commenters ask for the existing working schedule to be more flexible and cover other capture modes. |
| #1475 | high | Preserve movies by size | Asks to extend the existing preserve-movies setting to work by size. |
| #1441 | high | Inconsistent units | Asks to make units consistent in existing settings. |
| #1358 | high | Enhancement: Add camera direct UI to "Useful URLs" | Asks to add a camera UI link to the existing useful URLs. |
| #1355 | high | "Minimum Motion Frames" unit of measure: frames or seconds? | Asks to express an existing motion setting in time rather than frames. |
| #1349 | high | [cosmetic] Switch "Auto Threshold Tuning" should be before the two rel | Cosmetic request to reorder an existing settings switch. |
| #1339 | high | Enhancement: FTP upload testing by storing a screenshot | Asks that the existing FTP test leave a test file on the server. |
| #1322 | high | Don't show APPLY button if nothing has been changed | Asks to improve when the existing Apply button appears. |
| #1273 | high | Suggestion: Change font from Maven Pro to "system font" | Suggests changing the font of the existing UI. |
| #1217 | high | When make_message::list_media times out, the sent email ambiguously la | Asks that notification emails state a media listing timeout; a contributor agrees. |
| #941 | high | Shutter Speed | Asks to lift the shutter limit, which a comment ties to the minimum frame rate. |
| #852 | high | Support HTTP PUT method for motion notifications | Asks to add the PUT method to the existing webhook notification options. |
| #814 | high | Thumbnail image for motion movies | Asks to improve existing movie thumbnails using a Motion option. |
| #766 | high | Continuous Recording ignores Working Schedule | Asks that the working schedule also apply to continuous recording; only workarounds exist. |
| #736 | high | Problem : Not possible to do continuous video recording with stills on | Asks for continuous video alongside motion-triggered stills, which current continuous recording design does not allow. |
| #704 | high | Protect Admin Password Changes | Asks to add current password and confirmation checks to the password change. |
| #697 | high | Threshold percentage for motion detection | Percentage threshold is too coarse at high resolutions; asks for finer or absolute control. |
| #675 | high | Enable more stuff to be configured globally | Asks for global settings across cameras; the maintainer agrees it makes sense. |
| #565 | high | Ability to use both mask_file and smart_mask_speed together | Asks to allow two existing mask options together, which the UI currently forbids. |
| #319 resolved? | high | Rotating video changes orientation from landscape to portrate | Asks to improve rotation behaviour; the reporter later says it was implemented. |

## `documentation` (3, low 2)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #2522 resolved? | low | Gmail issues (30 May 2022/7 June 2022) | Gmail's authentication change prompts a request for an update or a note in the docs; a commenter says an app password method works. |
| #294 | low | Installation script | Offers an install script for the wiki and suggests apt packaging; could also be an enhancement. |
| #1338 | high | Wiki contribute: Arch simple install using AUR helper | Offers Arch install instructions for the wiki. |

## `CI/CD` (3, low 3)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #2624 | low | Project dependencies may have API risk issues | Automated-looking report about dependency version constraints in packaging; a commenter notes it concerns the old branch. |
| #2565 | low | motion_44 branch tools | Shares Docker build and container user changes for a branch, mainly about the build setup. |
| #1489 | low | Dockerfile uses Ubuntu 18.10 as base, which is EoL | Docker image base is end of life and a collaborator agrees to upgrade the images; bug would also be arguable. |

## `invalid` (1, low 1)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #787 | low | Created Ansible role for easy deployment | Announcement of a third-party Ansible role, with no question or problem. |

## `troubleshooting` (195, low 63)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #2907 | low | Smearing and green video | Video corruption was cured on one machine by a tip from another issue but persists on the NAS, so no overall cause is established. |
| #2818 | low | Webhook does not seem to be executed despite motion detection. | A collaborator only suspects an encoded space in the webhook URL by analogy with another issue, so the cause is not confirmed. |
| #2806 | low | USB storage - permission denied to write | Permission denied on USB storage; a collaborator asked for details and the cause was never established, though it may be a setup matter. |
| #2581 | low | no image on the web page when the Network Share (File Storage section) | No image when the network share is down, with no reply; could also be read as a request for better behaviour. |
| #2571 | low | switch port 8765 to other | Very short report that other ports fail on dev; a commenter asked for details and none came. |
| #2567 | low | Save image on motion detetection | Images sometimes missing from notifications; a collaborator lists possible known conditions but nothing is pinned down for this case. |
| #2543 | low | Telegram "Attached Images Time" affects when the webhook is called and | Clear observed interaction between Telegram timing and webhooks, but no faulty code named and no maintainer confirmation. |
| #1857 resolved? | low | Motion 4.2.2 not recording pictures or video | No capture on motionEyeOS after a clean install; another user's format change helped but the cause was never established. |
| #1855 resolved? | low | Can't stream by IP address.  Only by localhost | Port refused on the LAN IP; switching to Docker worked with the real cause unknown, and the listen setting was only a guess. |
| #1849 | low | MotionEye & Multicam Board | Multi-camera adapter board shows no camera, with no answer; could also be read as a how-to about unsupported hardware. |
| #1523 | low | Motioneye Remote Camera, two issues. | Remote camera lacks advanced settings and streaming URL, with no answer; this may be by design. |
| #1484 | low | Motioneye on Rasberry pi - high CPU usage | High CPU on a Pi, grouped with #1374; decoding is suggested as a possible factor but nothing was established. |
| #1481 | low | WebUI Rasbian install 8765 not reachable | Web UI port refused after a Raspbian install, no answer, similar to #1855 with no cause known. |
| #1430 | low | Camera resolution issue | Resolution limited on a Pi with a palette workaround and overheating; the cause was not established and the Chrome note covers only streaming. |
| #1427 | low | Unable to open video devices | Webcam cannot be opened; another user's codec change is offered but the reporter never replied. |
| #1414 resolved? | low | No camera image when a special character is inserted in text overlay s | Non-ASCII overlay text broke the image, but a collaborator could not reproduce it on dev and no fix is named. |
| #1400 resolved? | low | USB Webcam not supported? | Webcam gave no video; the reporter returned it and switched to an IP camera, so the cause was never established. |
| #1386 | low | Virtual Maschine - No image/stream from/to motioneye | No image in a VM; a collaborator discusses the Motion config and version but no cause was established. |
| #1379 resolved? | low | Not able to select camera while adding a network camera | Camera dropdown empties; one commenter says it works after an answer, while later users still see it and no cause is visible. |
| #1374 | low | Extremely high CPU usage | High CPU with many RTSP cameras; a collaborator only suspects Motion, without confirmation. |
| #1344 | low | Re-connected but still "enabled" video devices require manual interven | Reconnected cameras stay missing until the stream is opened; cause never established, with a suggested ping as an aside. |
| #1282 | low | Unable to add remote motioneyeos cameras | Remote camera lost after an update; a collaborator only guesses a missed config migration. |
| #1277 | low | When motion detection mask is enabled but empty, UI un-intuitively fai | Title-only report of UI failure with a missing mask file; not confirmed as a defect by a maintainer. |
| #1261 | low | Timestamp issues | Text overlay setting not respected after an upgrade done without the migration steps; cause of the overlay problem not established. |
| #1187 | low | Latest Version - Still Getting Admin Password Change Issues | Admin password overwritten through browser autofill; the maintainer asked to retest on a newer release and nobody confirmed. |
| #1155 | low | Motion detection on night vision | Night vision motion detection unreliable; only one tuning tip with no outcome. |
| #1124 resolved? | low | Email notification - character mapping must return integer, None or un | Test email encoding error; the reporter patched a Python library locally, but the true cause was not established. |
| #1114 | low | Hikvison camera not fluid | Frozen Hikvision image on a Pi 1; only guesses about hardware power or URL, no established cause. |
| #1111 | low | After reinstall rtsp capera gives green output | Green RTSP image after reinstall; one user's UDP over wifi experience is not confirmed as the cause here. |
| #1062 | low | Webhook replaces Command | A command mentioning a webhook gets moved to the webhook field; users share a workaround but no maintainer confirmed a defect. |
| #1046 resolved? | low | No camera on dropdown | Empty camera dropdown for an RTSP URL; the reporter found a workaround but the cause was never established. |
| #1014 | low | Video playback/download slow on motionEye+Raspbian compared to motionE | Slow playback on Raspbian compared to motionEyeOS; tmpfs suggestions did not settle the cause. |
| #1003 resolved? | low | playback/timelapse by phone and windows unavailable for motioneye crea | Files do not play on some clients, tied to an H.264 profile; a conversion script works around it but no defect was confirmed. |
| #970 | low | Connecting MotioneyeOS Camera to Motioneye Hub | Cannot connect cameras to a Docker hub on a Mac; the follow-up questions went unanswered. |
| #964 | low | Number of locally saved images do not match the number of FTP images | FTP uploads miss files; a contributor only believes retries are missing and suggests rsync. |
| #931 | low | Dark movie compared to streaming | Movies darker than the stream; the maintainer only redirects to Motion without naming a defect. |
| #922 | low | Can't add Panasonic webcam | Panasonic camera reported as unsupported; no answer, and the reporter suspects the URL. |
| #899 | low | recording size discrepancry between cameras | One camera records double the size of the other; no answer and no cause. |
| #888 | low | port 8081 doesn't stream | Stream port shows only a snapshot; the only comments were retracted as aimed at another question. |
| #857 resolved? | low | Strange colours / flickering with my connected network cams | Colour flicker never diagnosed; users report it gone after an OS switch or newer Motion and motionEye. |
| #840 | low | Extremely low FPS on Raspbian armhfp & Devuan ARM64. | Low frame rate report with only an unconfirmed tip about OMX encoding. |
| #834 | low | Unable to open Video Device, when it's dark outside | Video device error appears only in the dark; the cause was never established. |
| #833 | low | Google drive upload slows down | Upload backlog with several cameras; only a user's reading of the queue, not confirmed by a maintainer. |
| #818 | low | External storage problem | Uploads stop after setting an admin password; the maintainer explains a plausible path but no defect or fix is confirmed. |
| #753 + dup | low | Problem connection | Login lost for unknown reasons; a comment calls it the same issue as one in the motionEyeOS repo. |
| #692 | low | Automatic Brightness | Automatic brightness cycles from dark to white, with no answer or cause. |
| #691 | low | Output in two different folder places. | Files appear outside the camera folder, similar to #843; no cause established. |
| #678 | low | Lag between stream from rtsp camera and stream from raspberry. | Stream lag reported with questions but no answer or cause. |
| #670 | low | Raspberry Pi 3 | Text describes a camera setup on motionEyeOS with no answer; the same author reports D-Link trouble in #576. |
| #640 | low | 0.5 to 1 max FPS on raspian 8 + motioneye | Very low frame rate on a Pi Zero, with no answer, like #840. |
| #638 resolved? | low | Camera type problem | Network camera option missing; went away on an older OS with nobody establishing why. |
| #595 | low | gdrive uploads | Irregular Drive upload timing, pointed to the same backlog as #833 without a confirmed cause. |
| #558 | low | Video flickers in latest WebKit-based development browsers | Reporter is unsure of the cause and the maintainer only said they would look (agent: bug, changed in review) |
| #539 resolved? | low | Camera not adjusting to light conditions | Camera exposure only adapts after restart; a commenter only believes Motion is the cause, and the reporter worked around it with streamEye. |
| #536 resolved? | low | meyectl: ERROR: buffer is not large enough | Buffer error with no single cause: maintainer points to file corruption on a full disk for one user, and another cleared it by removing mask files. |
| #465 | low | Rasbperry Pi Camera as a Network Camera in a Server | Cannot add Pi cameras as network cameras; maintainer asks for logs and no cause was found. |
| #459 resolved? | low | corrupted mp4 files | Corrupted mp4 files over a long thread; a later user got it working by reinstalling, with no cause established. |
| #443 | low | mask creation and rotation of picture is inconsistent 2 | Follow-up saying mask with rotation is still inconsistent in actual use; no comments or confirmation. |
| #345 | low | Motion mask rb2 | Mask ignored; users retested newer builds without any confirmation, and it drifted into a corrupted data partition. |
| #327 | low | Raspberry Pi3 and 4x Logitech USB cameras | Multiple USB cameras fail; USB bandwidth messages appear but the cause was not settled, grouped with other multi-camera USB reports. |
| #317 | low | Noir Camera not working with motioneyeos | NoIR camera gives no picture; a defective unit is only guessed and the outcome of replacing it is unknown. |
| #267 | low | Motioneye fails to start on authorization failed error | motionEye fails to start on an authorization error; unconfirmed and another user has it with no solution, though better error handling is suggested. |
| #228 | low | Brightness problem | Brightness slider skips values near 50 percent, no answer; could also be an enhancement. |
| #2895 | high | Schermata Grigia anche con telecamera riconosciuta | Grey image from an RTSP camera with no reply and no known cause. |
| #2866 | high | DEV - No local Camera detection | Local cameras undetected with several confirmations across versions, but no cause was established. |
| #2855 | high | Videos Sometimes Have Blocky or Blurred Areas | Intermittent blocky video with only a generic suggestion from a passer-by and no known cause. |
| #2804 | high | p0w not recognizing camera 2 | Pi camera not detected on a Pi Zero W, with no reply and no known cause. |
| #2803 | high | Deepstack and Motioneye camera in Home Assistant | Deepstack face matching fails with the motionEye camera in Home Assistant, no reply and no known cause. |
| #2782 | high | Motioneye keeps starting more processes | Processes multiply in a Docker setup until the host hangs, with no reply and no known cause. |
| #2773 | high | Running Python-Script via Action Button Fails | A Python script fails only via an action button, with no reply and no known cause, like #2689. |
| #2745 | high | Motioneye freezes when adding a camera | Server hangs when adding a V4L2 camera in Docker; only a me-too reply and no known cause. |
| #2706 | high | raspberry pi camera v2 in motioneye container no image | Pi camera in a container cannot open the device; only a possibly related link and no established cause. |
| #2689 | high | "Run a Command" fails using discord_webhook in python script | A Python script fails only when run by the notification command, with no reply and no known cause, like #2773. |
| #2680 | high | MotionEye doesn't find USB pendrive | USB pendrive not listed under storage devices, with no reply and no known cause. |
| #2673 | high | Unable to open video device | Feed error on an RTSP camera while recording still works, with no answer and no known cause. |
| #2669 | high | Stranger video rendering | Odd video rendering in the web panel, with no reply and no known cause. |
| #2668 | high | Motioneye 0.42.1 , motion fails to start error, no camera feed anymore | Motion fails to start after a Home Assistant update, with no reply and no known cause. |
| #2653 | high | MotionEye on KDE Neon dosnt recognize camera | USB cameras and network access fail on a snap install, with no reply and no known cause. |
| #2636 | high | motionEye does not capture RTSP stream anymore after some months of se | RTSP capture stops after months of uptime, with no reply and no known cause. |
| #2628 | high | Can't zoom the image. | Zoom setting has no effect on a USB webcam, with no reply and no known cause. |
| #2607 | high | Droped frames | Dropped frames in recordings; a member asked to try the Python 3 version and no result or cause followed. |
| #2605 | high | Motioneye copid configuration | Two Pi installs appear to share configuration, with no reply and no known cause. |
| #2554 | high | Camera overview on iPad not correctly detecting landscape mode | Layout options missing on iPad, with no reply and no confirmed cause. |
| #2336 | high | Cannot mount network share | SMB signature error on a share; a member only suggests checks and no cause was established. |
| #2038 | high | Unable to scale streams to smaller size | Layout settings have no effect; a helper only speculates about mobile detection and no cause was established. |
| #2037 | high | Freeze OrangePi MotionEye | Freezes on an Orange Pi; the thread moves to upgrade attempts and no cause was established. |
| #1864 | high | motioneye not producing correct lastsnap.jpg symbolic link. | Lastsnap link not updated, called a bug only by the reporter, with no reply and no confirmed cause. |
| #1863 | high | Surveillance user login shows a white page | Surveillance login gives a white page, with no reply and no known cause. |
| #1856 | high | "Run a command" on motion detection not working (installed motioneye o | Run-a-command hook not firing on Ubuntu, with only a me-too and no answer. |
| #1852 | high | Works in docker, not with arch install instructions | No camera feed on an Arch install while Docker works, no comments and no known cause. |
| #1658 | high | Sometimes changing the framerate brings the camera back | Network camera drops and returns after a framerate change, with no answer and no known cause. |
| #1528 | high | Motioneye: From VMWare under Debian 9 to Docker | One of four cameras errors after migrating to Docker on Synology, with no answer. |
| #1509 | high | Segfault on Debian 9.11 | Segfaults where a contributor only guesses at a corrupted C library. |
| #1504 | high | On_event_end command sometimes does not stop | End command sometimes fails to stop a process; the reporter narrowed it to one camera config but no cause was established. |
| #1500 | high | USB and Network camera not displaying image. | Cameras detected but no image on Ubuntu, with no comments. |
| #1498 | high | Pi 3A+ // PiCamera FullResultion - no Emails / no Videos playable....a | No emails and unplayable videos at full resolution, with no comments. |
| #1493 | high | File format not recognized... | Recorded files not recognised by players; suggestions were given but no cause was established. |
| #1486 | high | Firefox Display Issue | Full screen display problem and other symptoms in several browsers, with no answer. |
| #1480 resolved? | high | Motion detection occasionally stops in running docker container | Motion detection stops in Docker; moving to a native install helped with the cause unknown, same as #1444. |
| #1463 | high | Clean Cloud - Deletes all previous day's folders if custom period used | Cloud cleanup deletes too much with a custom period; a me-too only, no confirmation or pinpointed code. |
| #1457 | high | Error loading web ui after logging in. | Web UI error after a router change, with no comments. |
| #1451 | high | Frame Rate | Frame rate limits and controls not working, with a me-too and no answer. |
| #1444 resolved? | high | Motion detected, but no snapshots/videos made anymore | Motion seen but nothing saved; it returned on its own and after a native install, cause unknown, same as #1480. |
| #1435 | high | Picture too bright with high resolution of Pi Camera | Overbright image at high resolution; only a restart workaround and a commenter's guess about the cause. |
| #1433 | high | motion.log being spammed in motioneye docker environment | Repeated debug lines fill the Motion log in Docker, with no comments. |
| #1420 | high | Doesn't work with slow camera's. | Slow network cameras drop out; a contributor only suspects Motion. |
| #1417 | high | Permission Denied in socket.py? | Service fails with a permission error after reboot, with no comments. |
| #1381 | high | Error adding motioneye camera | Error adding a camera after an OS update, with no answer. |
| #1378 | high | Two usb cams with motioneye 0.4 do not work | Only one of two USB cameras displays; the only explanation is a commenter's guess about USB ids. |
| #1331 | high | first 10sec of movie blank screen | Black start of every movie with one clarifying question and no cause found. |
| #1305 | high | Network Camera not working | RTSP stream fails; maintainer asked for a plain Motion test and no reply followed. |
| #1302 | high | Motion Detection doesnt seem to be working | Motion detection not firing; only tuning suggestions given and no outcome reported. |
| #1300 | high | Frame rate running, but greyed image on the dashboard | Grey camera image while frame rate runs, with no answer. |
| #1298 | high | Change setting and get Exec format error | Vague boot failure after changing settings, with no cause found. |
| #1283 | high | Saved movies in both .avi & .mp4 while set to HEVC (.mp4) | Movies saved in two formats; the reporter dropped the setup before any cause was found. |
| #1258 | high | Memory Leak in 0.40 | Memory growth in 0.40 reported with no cause found. |
| #1251 | high | Can't add xiaomi Xiaofang hacked camera | RTSP camera shows nothing though VLC works; several users, no cause found. |
| #1250 | high | FTP upload stops after one (or a few) uploads | FTP uploads stop until restart; one commenter's reinstall helped but no cause was established. |
| #1239 | high | MotionEye stream not fluid | Choppy stream on a Pi in Docker with no answer. |
| #1229 | high | Wrong path in %f variable when running a command | Unexpected path in the command variable for the reporter, with the cause never explained. |
| #1183 | high | MotionEye low framerate when streamed to Ubuntu VM ? | Low frame rate through a central VM server with no answer. |
| #1181 | high | ERROR: the maximum number of tasks (100) has been reached ( on a RPI3) | Task limit error tied to upload folder settings, with no answer. |
| #1180 | high | Motion detection deactivated but still triggering alarms | Motion detection switches back on by itself; others see it and no cause was found. |
| #1176 | high | No camera image when service run as user- Permission issues otherwise | Grey image after following the normal-user wiki steps, with no answer. |
| #1174 | high | "Segmentation fault " error on raspbian stretch | Segmentation fault where the maintainer only suspects Motion and ffmpeg. |
| #1169 | high | MotionEye 0.39.4 not sending picture in motion notification mail | Notification mails lacking pictures, with no answer or cause. |
| #1162 | high | Web Hook Stops working | Web hook stops until the service restarts, with no answer. |
| #1154 | high | Green Screen from time to time | Intermittent green screen; a commenter only guesses at overload. |
| #1146 | high | Camera Does not Require a Password | Error adding a camera without a password; the maintainer could not reproduce it and the cause is unknown. |
| #1144 | high | CPU 100% in browser viewing web interface of motioneye | High browser CPU and traffic from the web UI, with no answer. |
| #1135 | high | High CPU Utilisation since a few days | Sudden high CPU in Motion; only a suggestion to post elsewhere, with no cause found. |
| #1121 | high | Video Streaming | Images still reachable with streaming off, with no answer. |
| #1103 | high | Neither dropbox or google drive upload is working | Uploads fail despite a passing test; cause never found and the reporter moved to an own script. |
| #1097 | high | Streaming from webui works only after opening streaming port directly | Web UI stream only works after opening the stream port; the maintainer only guesses at MJPEG and the reporter disagrees. |
| #1085 | high | Cannot access Embed URL of remote Motioneye Camera | Embed URL fails for remote cameras, also after a reinstall and for another user; cause never established. |
| #1081 | high | Timelapse generation stuck saying "A timelapse movie is already being | Timelapse generation stuck in an already-running state; no cause found. |
| #1079 | high | Raspberry Pi 3 with Motioneye OS not Detecting Pi Camera | Pi camera not detected on motionEyeOS despite correct setup; no cause established. |
| #1075 | high | Motioneye crashes after a few hours on Raspi 3b+ | Crashes after hours on a Pi 3B+ with no cause established in the comments. |
| #1045 | high | Strange HTML output accessing my default cam page | Main page renders as raw output on one phone; no answer and no cause. |
| #1030 | high | Motion commands only process when restarting | Event commands appear to run only after reapplying config; no cause established. |
| #1029 | high | High CPU Usage and Frame Rate in Hundreds Sometimes Thousands | Abnormal frame counter and high CPU; a contributor asks for tests and no cause follows. |
| #1012 | high | USB cctv camera not working? | Detected USB camera does not work and there is no answer. |
| #992 | high | Stream issues | Stream fails while a third-party dashboard accesses it; no answer. |
| #991 | high | Stream Freeze Loops every ~15 seconds | Periodic stream freezes described with no answer. |
| #987 | high | Xiaofang (Fang-Hacks) | RTSP server on a hacked camera crashes; the maintainer asks for details and no cause follows. |
| #985 | high | Cannot save pictures nor movies. | No pictures or movies saved; settings look right to the maintainer and logs were never analysed. |
| #976 | high | MotionEye on raspbian: no camera detected | Camera not detected on Raspbian; only an unanswered suggestion followed. |
| #968 | high | Unable to open video device | Unable to open video device with many RTSP cameras; no answer. |
| #958 | high | Extremely low framerate selecting HEVC | Very low frame rate with HEVC on a Pi 3; no answer. |
| #956 | high | Microsoft LifeCam Studio USB web cam not detected | USB webcam stopped working after an update; no answer. |
| #944 | high | on_event_start is triggered even if motion detection is OFF | Event command runs with detection off; no comments and no cause. |
| #936 | high | Problem adding network camera - motioneye on Ubuntu Server 16.04 | Network camera not added properly on Ubuntu; no answer. |
| #933 | high | Los of video feed | Video lost about every 18 hours until reboot; another user's client setting does not establish the cause here. |
| #927 | high | systemctl status motioneye, returns: failed! Result: exit-code***** | Service fails on start with a traceback; no answer or cause. |
| #923 | high | Jerky video after 1 second | Recording turns jerky after a second on a Pi Zero; no answer. |
| #917 | high | No red frame while recording | Missing red frame while recording; a reboot helped someone else and no cause is known. |
| #912 | high | unable to open video device - invalid data found | Unable to open video device for one RTSP camera in Docker; no answer. |
| #901 | high | RTSP stream losing connection to the camera in a loop | RTSP reconnect loop in Docker; only a request for logs followed. |
| #871 | high | Docker container keeps restarting | Container restart loop on ARM; a collaborator only says the image may be broken. |
| #867 | high | Suddenly stoped recording | Recording stopped suddenly; the maintainer only suspects overheating. |
| #866 | high | Cameras stop recording, but I still see them | Cameras stopped recording, reinstall attempted, and no cause was found. |
| #859 | high | 2nd camera upload to Google Drive and motion detection upload | Google Drive setup fails for a second camera, with no answer. |
| #843 | high | not save image | Files not saved where expected; a collaborator only suggests a possible root directory cause, unconfirmed. |
| #837 | high | Motioneye on Ubuntu showing camera 1 image on 1 and 2 on main page | Wrong camera image shown on the main page, with no answer. |
| #824 | high | FTP problem | FTP upload stops after days with no logged error and no answer. |
| #823 | high | Camera not usable - WARNING: Connect error on fd 15: ECONNREFUSED | Connection refused warning with an unusable camera; several users affected and no cause found, same message as #756. |
| #806 | high | Problem with GDrive upload when MotionEye automatically start | Drive upload fails when started as a service; suggested fix did not help and the cause is unknown. |
| #768 | high | Motioneye not start (status=1/failure) | Service fails to start; only a guess about tornado was offered. |
| #767 | high | Motioneye stops after sometime | Server becomes unreachable from time to time and no cause was found. |
| #756 | high | WARNING: Connect error on fd 16: ECONNREFUS causing many false alarms | Connection refused warnings with false alarms and no answer, same message as #823. |
| #735 | high | Randomly change video bitrate to very low [50~300 KiB] on Raspberry 3 | Random bitrate drops reported with no answer. |
| #722 | high | View movies stored on external disk | Movie list keeps loading for external disk media, with no answer. |
| #717 | high | RTSP not reconnecting | RTSP does not reconnect after signal loss; the reporter only suspects Motion and no cause was named. |
| #706 | high | The timelapse movie could not be created | Timelapse creation and preview errors reported with no answer. |
| #686 | high | no motion detected running in docker | No motion detected in a Docker setup and no cause found. |
| #645 | high | Errors in log | Repeating exception floods the log; the maintainer cannot explain it. |
| #642 | high | Dont works notifications | Notifications never fire, with no answer. |
| #641 | high | bad image | Green RTSP image with only a suggestion to try other ffmpeg versions. |
| #639 | high | When # images is large, hitting "zipped" never actually downloads them | Zipped download hangs with many images, with no answer or diagnosis. |
| #609 | high | movie problem. | Recorded movies do not play, with no answer. |
| #608 | high | Unit motioneye.service entered failed state. | Service fails on openmediavault and the cause was never established. |
| #603 | high | Impossible to send mails notifications | Mail notification timeout with no diagnosis; later comments only share another mail setup. |
| #576 | high | DCS-932LB camera | Connection to a D-Link camera lost, with no answer. |
| #575 | high | green tinted images | Green tint recurs; users share camera parameter workarounds but no cause is established. |
| #567 | high | Continue recording and motion | Long movies play back too fast since Motion 4, with no answer or confirmed cause. |
| #546 | high | Brightness of on RPI Zero W with PiCam NoIR 2? | Brightness goes wrong at higher Pi camera resolutions; no cause established. |
| #516 | high | issue: motioneye on Ubuntu with more than 1 Microsoft usb cams | Only one of several USB cameras opens; users only speculate about USB or drivers. |
| #487 | high | RPI 2 Camera quality | Washed-out Pi camera image on a manual install; reporter reverted to the image and the cause stayed unknown. |
| #411 | high | Image motion detection works.....Video trigger not | Motion-triggered movies do not work while pictures do, even after moving to motionEyeOS; no cause found. |
| #401 | high | MEye saves images locally but will not upload to either Dropbox or Goo | Uploads to Dropbox and Drive fail; maintainer could not figure out why from the logs. |
| #385 | high | lost picture - pink | Pink distorted image; a commenter only guesses at hardware from their own experience and the reporter never replied. |
| #381 | high | Email & webhook notifications have stopped | Notifications stopped; maintainer only suspects SD card corruption. |
| #357 resolved? | high | Motioneye stopped reacting on motion | Motion events stopped triggering; users report differing workarounds such as changing movie format, with no cause established. |
| #335 | high | Conflict between 2 USB webcam | Two identical USB cameras conflict, no answer. |
| #170 | high | Motion detection not working on rtsp-cams ? | Detection on RTSP cameras stops over time; a long thread reached no established cause. |

## `question` (180, low 41)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #2715 | low | triggering raw pictures | Unanswered question whether the code can be altered for raw pictures; could be read as a feature request. |
| #2634 | low | high usage of motioneye processor on raspberry pi 3 model b | Asks why CPU is at 100 percent on a Pi 3; only a user's hardware access tip, grouped with other CPU decoding load reports. |
| #1842 | low | Integration with motion api and status reflection on motioneye | Asks how to use the Motion API and have the status reflected in motionEye; could also be an enhancement request. |
| #1531 | low | Ezviz C4s Dome Cam - grey screen Unable to open video device | Specific camera not opening over RTSP; comments point to camera firmware and setup, though the visible text is partial. |
| #1503 resolved? | low | motioneye service will not start in Fedora 30: Error: pycurl: libcurl | Same pycurl SSL backend install error as #1483, fixed by reinstalling pycurl; the reporter also suggests a docs update, so documentation is close. |
| #1499 | low | Unable to access MotionEye stream from the Internet | Reaching the stream from the internet is a network setup matter, but it remained unsolved. |
| #1491 | low | Try to downgrading Motioneye | User seeks help downgrading to an older version after an incompatible upgrade, with no answer. |
| #1482 | low | Nginx tutorial not working without base_path | Nginx reverse proxy setup; a commenter points to the URL form, as in #1532, though the tutorial could also need a docs fix. |
| #1477 | low | Pycurl problems ? | Service fails on a pycurl import, apparently the same install problem as #1483, but it has no answer and the error text is cut off. |
| #1447 | low | Momentary action button ? | Short unanswered is-it-possible about a momentary action button; could also be a feature request. |
| #1393 resolved? | low | Upgrade results in camera no longer being configured | Cameras lost after upgrading to 0.40; commenters point to a config migration script, though bug or documentation is arguable. |
| #1382 | low | My method of Uploading to OneDrive using RCLone with MotionEye trigger | User shares an rclone upload method and asks whether this is the right place, with no defect reported. |
| #1347 | low | Run a Command - nothing happens | User script not run by Run a Command; the only answer points at file permissions, unconfirmed, as in #1192. |
| #1332 | low | Feature to upload a snapshot as soon as movement is detected | Requested snapshot on motion; the maintainer answers to use Run a Command, though a feature label would also fit. |
| #1326 | low | Motioneye cannot access /media/username mounts | Unanswered Docker storage path setup question, likely a configuration matter but never stated. |
| #1270 | low | After Upgrade: Setting current date using http: failed | motionEyeOS date and access problem like #1350 and #1291; the maintainer points at the network adapter setup, only as a possibility. |
| #1255 | low | Is there a way to enable streaming only when needed ? | Asks if on-demand streaming is possible, with only a cron workaround; could also read as a feature request. |
| #1233 | low | Still Cleanup does not work | Cleanup not removing files; a contributor points at the Preserve settings, and the reporter did not confirm. |
| #1232 resolved? | low | Cannot install on Raspberry PI Zero | Install memory error on Pi Zero, answered by disabling the pip cache because of Pillow's size. |
| #1192 | low | "Run a command" not working. | User script not run by Run a Command; commenters point at command path and user setup, as in #1347. |
| #1145 | low | Support  usb capture card | Unanswered how-to on using a USB capture card, titled like a support request. |
| #1128 | low | unexpected keyword argument 'camera_id' | Error from an old tornado version per the maintainer, same fix type as #1243; the upgrade outcome is unreported. |
| #1123 | low | Start/stop a single camera (to reduce the total CPU load) | Asks if one camera can be stopped by command; a commenter gives script pointers, though a feature label could fit. |
| #1122 | low | Pi Zero w CPU constantly high | High CPU on a Pi Zero answered with frame rate and Fast Network Camera advice, pointing at hardware limits. |
| #1095 | low | motioneyeos is cooking my raspberry | Asks why five cameras load and heat a Pi; no defect found, same kind of load question as the other CPU issues. |
| #1089 resolved? | low | Motion Eye not saving Video | No media saved; commenters point to the codec and another user fixed it by choosing a different movie format. |
| #1051 | low | CPU Question | Asks about CPU load when recording several HD streams; discussion concerns hardware limits and Motion, no motionEye defect. |
| #1050 | low | second ethernet port for IP cameras | Network setup question that drifts into stream log errors; the reporter takes them to the Motion community. |
| #995 | low | Streaming URL not available in docker. | Asks how to reach the stream URL from Docker; a host network tip is given and a collaborator notes a missing wiki port. |
| #982 | low | Motioneye and VLC | Asks why own VLC tag page modification shows artifacts with many streams; no answer. |
| #974 | low | Change default time change | Asks how to change the default time after a restart without internet; no answer. |
| #957 | low | Is full access to Dropbox necessary? | Asks whether full Dropbox access is needed; the maintainer does not know and invites suggestions. |
| #900 | low | motioneye does not start on startup (raspbian) | Own autostart attempts fail; a commenter points to the install guide step that sets this up. |
| #820 | low | Cannot find mass storage | motionEyeOS storage option depends on a camera being attached in this setup; no motionEye defect found. |
| #804 | low | motioneye camera noir with ir - white screen | White screen in the dark traced by the reporter and a contributor to power and attached hardware. |
| #666 | low | USB Webcam not detected | Camera works on a Pi but not in an Ubuntu VM; a contributor points to VM USB handling. |
| #660 | low | ftp server saves also on SD CARD | Starts as how to configure storage for FTP only, then drifts to setup checks on the user's side. |
| #628 | low | Digest Authentification | Asks if digest authentication is supported; a user reports RTSP as a working alternative. |
| #449 | low | MemoryError gdrive uploading file > 300 MB | Maintainer explains it as running out of memory on 1 GB RAM, no defect named (agent: bug, changed in review) |
| #442 resolved? | low | Picture misformed // what are best options to reduce cpu | Reporter traced it to high CPU on their Pi and asks how to reduce it (agent: external bug, changed in review) |
| #400 | low | Allwinner H3 devices support | Asks about H3 hardware encoding; maintainer answers that accelerated ffmpeg libraries already carry over, though it could count as a feature request. |
| #2880 | high | Tapo PTZ cameras | Asks how to add PTZ action buttons for Tapo cameras; the only reply gives pointers to other projects. |
| #2875 resolved? | high | Latest image for command to run on motion | How-to answered by a collaborator with the lastsnap symlink, and the reporter says that works. |
| #2868 | high | Unable to connect to IP camera Internec i6.4-C series | Connection problem from credentials embedded in the URL; a member explains to use the input fields instead. |
| #2867 resolved? | high | DEV - Port 80 not working | Port 80 is a privileged port for the non-root service; a commenter explains and gives a reverse proxy workaround, so no defect. |
| #2860 | high | Inquiry about software compatibility with DVR Dahua HCVR5108HE-S3 and | Unanswered compatibility question about a specific DVR on a Raspberry Pi. |
| #2858 resolved? | high | Multiple Camera view | Asks about a fullscreen multi-camera view; a collaborator says it does not exist and the reporter built their own page. |
| #2834 resolved? | high | Take picture with proximity sensor | Asks how to trigger a picture from a sensor; a commenter gives a working snapshot URL command. |
| #2825 | high | Delay to generate the symbolic Link Lastsnap | Lastsnap timing is answered by a collaborator as a Motion behaviour adjustable through the capture mode setting. |
| #2817 | high | Raspberry Pi Zero W2 | Asks about a compatible image for a board, answered with a motionEyeOS fork. |
| #2814 | high | Unable to see the stars and no way to adjust the exposure! | Asks how to adjust exposure on motionEyeOS for night sky use; a commenter points to raspicam parameters. |
| #2809 | high | Cannot find mass storage on the web gui | Mounted disk not listed in the UI; a collaborator gives the Custom Path option. |
| #2797 | high | How to save files to a network drive | Plain unanswered how-to about saving to a network drive. |
| #2794 | high | How can I send telegram notifications to an specific topic? | Unanswered how-to about sending Telegram notifications to a specific topic. |
| #2791 | high | BeaglePlay | Asks whether a board's video hardware can be used on a dev motionEyeOS build; a collaborator explains options. |
| #2779 | high | Motioneye & Raspberry PI4B 8 Gb | High CPU on a Pi 4 is explained by a collaborator as depending on config and CPU video decoding, so no defect. |
| #2762 | high | Impossible to add a new network camera | Report concerns a different fork installed from elsewhere; a member says wrong repository and to install dev here. |
| #2677 | high | No filesystem created during installation | Install with an older wiki guide left no config; a member points to the current installation instructions. |
| #2670 | high | versions where motioneye runs | Unanswered question about supported OS versions and architectures. |
| #2661 | high | Moviepasstrough - main stream/second stream | The wish for a separate recording stream is answered by a collaborator with an existing Motion parameter. |
| #2652 | high | Rights to write file (recordings or stills) | Write permission error answered by a collaborator with commands to grant folder access to the service user. |
| #2637 | high | parallel video recording | Asks how to record continuously alongside motion clips; a collaborator says it is unsupported and workarounds are given. |
| #2630 resolved? | high | VA-API supported? | Asks whether VA-API is supported; the reporter works it out with the dev branch and Motion 4.4. |
| #2622 | high | Motioneye on pi 3 uses 100% on one core with very poor framerates | Asks how to use multiple cores and GPU acceleration; a collaborator explains the state of hardware acceleration. |
| #2617 | high | Interfacing with RaspiStill | Unanswered question whether anyone feeds still images into motionEye and how. |
| #2616 | high | Not clear how FPS mismatch b/w UI and (sub-)streams affect CPU usage | Asks how frame rate settings interact; a collaborator discusses configuration and no defect is found. |
| #2582 | high | Third version of wifi chip Rpi0 2 W using motioneye Jaspers image | Asks a third-party motionEyeOS image builder for WiFi support on a board revision, which concerns another product. |
| #2569 | high | Webinterface | Asks where the web interface files are stored; no answer. |
| #2568 | high | Noob alert! - Motion Detection and File Sizes | A new user asks for help with motion detection and file size settings; no answer. |
| #2559 | high | Very high load, low FPS, etc | Asks which settings lower load with six cameras on a Pi 4; users suggest settings and no defect is found. |
| #2558 | high | MotioneyeOs on RPI Zero 2W randomly connects/disconnects to WIFI | WiFi drops on a motionEyeOS fork on a Pi Zero 2W concern another product, with no defect found. |
| #2556 resolved? | high | Error : Format not supported or inaccessible/unsuitable for playback | H265 playback failure is solved by the reporter through lower quality and disabling passthrough, as a collaborator advised. |
| #2506 | high | raspberry with MotionEyeos and PIR Sensor | Asks how to use a PIR sensor; a collaborator says no direct support and links workarounds. |
| #1938 | high | Getting an Auto Focus Pi Camera to auto focus on Motioneye | Unanswered question whether autofocus can be configured for a specific camera. |
| #1859 resolved? | high | Videos too heavy | Large video files are a settings matter; the reporter found a solution by lowering movie quality. |
| #1848 | high | opacity value variation | Asks what varying opacity values on the login page mean, with no defect reported. |
| #1845 | high | Get access to Action buttons from external application | Asks how to call action buttons from an external application, and nobody answered. |
| #1808 | high | Ftp Upload / Weathercam / Weatherunderground / Help | Help setting up FTP upload to a weather service; a collaborator explains the test button and the log suggests upload works. |
| #1643 | high | Limited options on Ubuntu Server | Missing update and reboot options are explained by config file settings and running as root. |
| #1532 resolved? | high | Reverse proxy on Apache returns only text | Apache reverse proxy configuration; commenters explain the trailing-slash setup and one got it working. |
| #1524 | high | lost mmal service 16.1 | Asks whether a version includes an mmal camera service and how to install it. |
| #1520 | high | Multiple motion pi set up | Plain how-to about showing one Pi's camera on another Pi. |
| #1505 | high | permanent offline use? | Asks how to run offline as a DVR and was pointed to existing guidance. |
| #1487 resolved? | high | Minor issue or bug: cannot scale text overlay for one cam only | Text scale problem was resolved by a commenter updating Motion. |
| #1483 resolved? | high | Fedora 30 "Exit-code" / "ImportError: pycurl: libcurl link-time ssl ba | Pycurl SSL backend error on Fedora, solved by the reporter reinstalling pycurl as a commenter pointed out. |
| #1476 | high | is it possible to make google home mini say a phrase when motion is de | How-to about using a webhook to make a smart speaker talk. |
| #1471 | high | How to create a switch for shutting down motioneye OS | How-to about a shutdown switch script on motionEyeOS. |
| #1467 | high | Grabbing the pixel count deltas | Asks where a pixel count comes from; a collaborator explains that Motion draws it. |
| #1461 | high | Motion Detection not working with night vision | A comment explains the night camera needs infrared illumination to see motion, a setup matter. |
| #1460 | high | Snapshot via Console | Asks how to take a snapshot from the console. |
| #1454 | high | script for add PTZ? | Asks for help scripting a pan-tilt setup. |
| #1442 | high | [HELP] Turn FNC on/off via terminal/config | Asks how to toggle Fast Network Camera from the terminal or config. |
| #1439 | high | Raspberry Pi zero W fails to start motioneye | motionEyeOS boot failure posted in the wrong repository, as a comment says. |
| #1418 | high | Did the API ever get implimented (how to change setting with get/post) | Asks whether an API exists and how to change settings or take snapshots with HTTP requests. |
| #1416 | high | Timelapse defaults | Asks how to change timelapse defaults. |
| #1392 resolved? | high | usb&remote cameras no action on motion | Motion triggering not saving files was fixed for a commenter by changing noise and light settings. |
| #1387 | high | Action Button via URL from Server to the GPIO pin on network camera. | How-to about driving a GPIO pin on a network camera with an action button. |
| #1364 resolved? | high | Execute Script after detecting Motion | How to run a script on motion; a commenter explains the file location that worked. |
| #1352 resolved? | high | Motioneye missing files thread0.conf in Pi Zero W | motionEyeOS setup problem the reporter worked out; a collaborator redirected it to that project. |
| #1350 | high | motioneye setting date failed !! | motionEyeOS date setting problem; a collaborator says it is system configuration, not motionEye. |
| #1336 | high | What movie format in motioneye uses least cpu? | Plain unanswered question about which movie format uses least CPU. |
| #1330 | high | Wifi Off? | How-to about running without WiFi, answered by connecting through localhost. |
| #1291 | high | Manual IP address (static IP), the displayed date is 1970-01-01 | motionEyeOS date wrong with static IP; answers point at the user's gateway and NTP network setup. |
| #1281 resolved? | high | Question on frequent cameras lost connections | Reporter asked about lost cameras and mitigated them by changing their own WiFi and DHCP network. |
| #1269 resolved? | high | Migrate from RPi3 to RPi zero | Camera on a Pi Zero was a wiring and voltage matter; the reporter says it can be closed. |
| #1268 resolved? | high | No video streaming from Camera | Old packaged versions on Ubuntu; a commenter with the same issue fixed it by installing a newer Motion. |
| #1257 resolved? | high | Multiple devices with a central server, grey screen | Remote stream failure solved for the reporter by a Motion netcam setting. |
| #1256 resolved? | high | BUG upgrade from 0.39 to 0.40 | Upgrade to 0.40 loses cameras unless the migration script from the release notes is run, which commenters confirm works. |
| #1253 | high | Set up an alert when a camera connection loss | How to alert on camera loss, answered with Motion event options. |
| #1252 | high | Straight Rip of RTSP Stream | How to record high resolution without transcoding, answered with Motion options by a collaborator. |
| #1243 | high | Failed to start on Debian Jessie | Install failed to start; the maintainer answered with the tornado version to install, as in #1128. |
| #1236 resolved? | high | Pimoroni pantilt hat integrated into Motioneye? | Asks how to control a pan-tilt hat; a commenter shared working scripts using action buttons. |
| #1213 | high | Overriding config values | Asks how extra Motion options interact with the threshold slider setting. |
| #1203 | high | lighttpd reverse proxy | Unanswered how-to on running behind a lighttpd reverse proxy with a base path. |
| #1141 | high | Question: Network camera problems. | Unanswered question about understanding camera types and network setup. |
| #1133 | high | Command to wake up Display | User script cannot open the display from Run a Command; answered with an Xauthority pointer. |
| #1131 | high | FNC and then no web interface? | Fast Network Camera access problem; the maintainer says it belongs to motionEyeOS. |
| #1117 | high | NTP freezes startup | NTP boot hang on motionEyeOS; a collaborator points to the separate motionEyeOS project and no motionEye defect is found. |
| #1113 | high | motionEYE: Actionbutton for Dlink DCS-5000L | Asks whether anyone has configured action buttons for a specific D-Link camera; no answer. |
| #1084 | high | writeimage.sh does no run when i use the run command | Writing the motionEyeOS image on macOS; answered as a wrong directory or use of another tool. |
| #1061 | high | openmediavault motioneye docker on the raspberry pi device? | Plain install question about the OpenMediaVault Docker on a Pi; no answer. |
| #1052 resolved? | high | video download issue | A maintainer explains such a large file cannot be handled on a Pi and how to remove it manually. |
| #1025 resolved? | high | How to send Image/Movie or Filename via WEBHOOK | How-to on webhook data; the reporter found they can pass the filename. |
| #1010 resolved? | high | when making a MotionEye Server? | Hardware sizing question answered directly by a maintainer. |
| #1002 | high | Running Motioneye as normal user | Asks which files to copy when following the normal user wiki guide; no answer. |
| #988 | high | CPU consumption | Asks why CPU is high when idle; a maintainer explains possible normal causes. |
| #967 | high | [NOT ISSUE] Trigger video / image saving manually [NOT ISSUE] | Reporter marks it as no issue and asks how to trigger saving manually by script. |
| #960 resolved? | high | Use GPU on Odroid XU4 | How to use hardware encoding on an Odroid XU4; a contributor gives the encoder setting. |
| #952 resolved? | high | Admin page not accessible | Forgotten admin password; a maintainer gives the reset steps. |
| #951 resolved? | high | motioneye service doesn't work | Service fails after a non-root pip install; installing as root helped a later commenter. |
| #950 resolved? | high | Motion Alarm Emails do not contain image attachments | Email attachments setting; the maintainer answers with a link to the FAQ. |
| #943 | high | On Raspbian during installation | Install step fails on a missing ffmpeg package and asks for a workaround; no answer. |
| #902 resolved? | high | Raspbian - No USB Cameras | No USB cameras after install; the maintainer says to install Motion, a setup step. |
| #896 | high | Some issues with MotionEye | motionEyeOS complaints posted in the wrong repository, as a comment notes. |
| #892 | high | Performance diference between OrangePi Zero H2+ and RPI Zero v1.3 | Asks to compare performance of two boards before buying. |
| #872 resolved? | high | Ubuntu 18.04 LTS | Stale pycurl build after an OS upgrade; clearing the pip cache and reinstalling fixed it for several users. |
| #868 | high | Possible to get MotionEye Loaded into BlueIris Surveillance Software | Asks how to feed a motionEye camera into Blue Iris; only suggestions followed. |
| #842 | high | How can i capture on_camera_lost | Plain how-to about hooking the camera lost event, unanswered. |
| #826 | high | reduce light "spot" | Asks how to reduce lamp glare; answered with physical changes on the user's side. |
| #803 | high | Multiple devices with a central server | Asks whether a central hub can do detection for remote cameras. |
| #794 resolved? | high | Very Good Software, just one issue with pi cam locally | The reporter found the Pi camera itself faulty and is returning it. |
| #747 resolved? | high | Jessie to Stretch Upgrade, pip install motioneye fails due to lack of | Install failure from missing zlib headers, fixed by the reporter installing packages. |
| #743 resolved? | high | motion not detected | The reporter got motion detection working by changing settings. |
| #728 resolved? | high | fast network camera not working anymore | The reporter found the stream works in Chrome and not IE11, then asks how to add the camera elsewhere. |
| #716 | high | Unable to Start Motion on Ubuntu | The maintainer explains the start error as starting the service twice, a user-side cause. |
| #700 | high | GPU OR CPU | Asks how to tune GPU memory and overclocking settings. |
| #693 | high | MotionEyeOs and V4L2 Camera on RaspBerry Pi3 | The reporter says this belongs in the motionEyeOS repository. |
| #690 resolved? | high | E: Unable to locate package libavresample2 | Install step fails on a missing package; the reporter solved it by following a forum thread. |
| #671 | high | saving files to usb-stick | USB stick not used after replugging, explained by the lack of automounting on the system. |
| #669 resolved? | high | How to stream with motioneye trough a GSM proxy/ firewall? | How-to on remote access behind GSM; the reporter solved it with a tunnelling service. |
| #664 resolved? | high | MotionEye does not show camera images when I access from Internet! | Remote image missing because of port forwarding; a user solved it by also forwarding the stream port. |
| #659 | high | Notification on / off via Command line? Bash script? | How-to on toggling notifications from the command line, answered with workarounds. |
| #646 | high | Backyard bird activity | Pi does not recover after solar power loss; the advice concerns the user's power setup. |
| #637 | high | Video on "wired PC" but not working on wireless | Access differs by device; a contributor places the problem in the user's router settings. |
| #627 | high | Mask and Threshold | Asks how threshold and mask interact; a collaborator explains it. |
| #610 | high | Upload media files to gdrive | Asks how Google Drive upload timing works, unanswered. |
| #554 resolved? | high | motion rapstill | How to take a snapshot while the daemon runs; reporter succeeded with the Motion HTTP API. |
| #540 | high | Computer Build for MotionEye | Asks what CPU is needed to run motionEye. |
| #535 | high | how to run ? py script in motioneyeos ?? | How to run a Python script on motionEyeOS; a user gave the answer. |
| #529 | high | Motion detection (Parking IOT) | How to tune detection output and crop the camera image. |
| #526 | high | Can't connect to wifi | WiFi dongle setup on motionEyeOS; no motionEye defect found. |
| #521 | high | intervalle 20-25 fps | Asks which setting gives a higher frame rate on a Pi camera. |
| #514 resolved? | high | Amcrest IPM-741 | Camera settings question; several users thank a commenter whose answer worked. |
| #501 resolved? | high | Monitoring Commands from GPIO pins | How to write a monitoring command script; an example was provided and the reporter can use it. |
| #495 resolved? | high | Problem DIGOO rtsp Camera | RTSP camera add failed until the correct stream type setting was chosen; reporter confirmed it works. |
| #479 | high | Failed to connect wifi cam RaspberryPi Zero W | Reporter misunderstood that the remote Pi must also run motionEye; maintainer explained the setup. |
| #477 | high | multiple file storage | External flash drive storage setup; a commenter asks if it was mounted and says it is not a motionEye issue. |
| #439 | high | How can I auto (re)connect to a camera stream? | Plain how-to on auto reconnecting to a camera stream, no answer. |
| #428 resolved? | high | Motion triggered movies. | Frozen looking movies were a VLC preference, as the reporter found. |
| #423 | high | Whitebalance and ISO shutter-time | Asks how to adjust white balance and shutter time; answered with extra Motion options and post-processing. |
| #414 | high | Archer T2UH usb | How to get drivers for a WiFi dongle on motionEyeOS, which lacks them. |
| #363 | high | How to limit still images | How to limit still images per detection, no answer. |
| #358 resolved? | high | Preserve Pictures and Dropbox | Asks if local retention affects Dropbox; maintainer says it never deletes there and the reporter found a workaround. |
| #320 | high | How to properly detect motion | How to tune detection settings; a collaborator explained thresholds versus resolution. |
| #308 resolved? | high | Start service. | Service failed from a wrong ffmpeg install; following the wiki again fixed it. |
| #307 resolved? | high | Is there a way to see unsuccessful attempts to log in in logs? | Asks how to see failed logins; a member showed the journal commands, which work with fail2ban. |
| #306 resolved? | high | System Won't Update | Update appeared stuck because of the pre-release setting; explained by the maintainer and the reporter's systems now update. |
| #262 | high | Frame Rate Hight - Slow picture | Asks how to optimise frame rate at high resolution; advice given to lower resolution or use fast network camera. |
| #256 resolved? | high | sendmail is clogging up, email notification stops | Maintainer attributes it to too many stored media files; the reporter applied a cleanup solution. |
| #214 | high | Adjusting brightness from shell script | How to change brightness from a script; a user shared a working approach. |
