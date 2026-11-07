# Closed unlabelled issues, batch 3 proposal

932 issues (#1941 to #2), classified by 9 agents on 2026-11-07 from the body and the last 3 comments. Nothing applied yet.

Sample check: 40 random issues judged without seeing the proposal: 25 of 25 high confidence agree, 13 of 15 low confidence agree.

| Label | All | Low confidence |
|---|---:|---:|
| `bug` | 76 | 24 |
| `external bug` | 18 | 14 |
| `feature` | 62 | 18 |
| `enhancement` | 50 | 20 |
| `documentation` | 26 | 5 |
| `meta` | 3 | 1 |
| `CI/CD` | 3 | 3 |
| `invalid` | 20 | 5 |
| `troubleshooting` | 201 | 74 |
| `question` | 473 | 97 |

## `bug` (76, low 24)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1843 | low | Send motion notification to MULTIPLE webhook URLs | Semicolon in webhook breaks config parsing; collaborator made PR |
| #1827 | low | camera_id not present in config files - Motion using thread number ins | Reporter pinpoints motionctl.py camera id versus thread id mapping |
| #1774 | low | Trying to lower frame change threshold results in no motion detected a | 1% threshold written as invalid threshold 0 in config |
| #1625 | low | Python 3: unicode() --> six.text_type(), NOT six.u() | Pinpoints wrong Python 3 conversion; closed by linked PR |
| #1607 | low | Google Photos Upload Stops Working | Shared motionEye project token hits quota; users patch own token |
| #1599 | low | Too many bare exceptions in the codebase | Code quality issue with bare exceptions; fixed via linked commit |
| #1597 + dup | low | MotionEye SMTP Password isn't escaped | Unescaped SMTP password crash; collaborator marks duplicate of #1399 |
| #1541 | low | Security risk for your Google Drive account | Google Drive access issue; maintainer tracks it, later working |
| #1469 | low | No video feed from a USB cam | Chrome update broke image streaming; see #1401 (agent: external bug, changed in review) |
| #1428 | low | Video stream not visible in main UI | Chrome 76 lazy loading clash; fixed in motionEye 0.41rc1 |
| #1422 | low | Motioneye captures photos and video to disk but not visible in UI | Live view failing only in Chrome 76; another browser works (agent: external bug, changed in review) |
| #1415 | low | Camera Works Outside MontionEye - MotionEye doesn't add it | Chrome update broke streaming; Safari works (agent: external bug, changed in review) |
| #1412 | low | Spinning icons instead of camera feed | Chrome update broke image streaming; other browsers work (agent: external bug, changed in review) |
| #1405 | low | Camera suddenly not recognising on any of three motioneye pi's | Chrome update caused it; changing Chrome setting solved (agent: external bug, changed in review) |
| #1401 | low | MotionEye - does it run on Chrome 76.0.3809.100? | Chrome 76 broke streaming; updating motionEye fixed it |
| #1197 | low | Doorbird - Unable to open video device | Unauthenticated device scan triggers 429; collaborator suggests reordering UI fields |
| #1070 | low | motion 4.2 | Motion 4.2 incompatibility; maintainer links fix release 0.40rc1 |
| #783 | low | Only able to add a USB camera as first camera, before RPI cam | Reporter confirms working after apparent fix; details not visible |
| #622 | low | [Feature request] FIX Time Zone and Clock Format | Wrong Caracas timezone; thingos commit fixes motionEyeOS, not motionEye |
| #348 | low | Cards with multiple inputs ? | Support question, but commit fixes multiline extra options in Firefox |
| #141 | low | motioneye service fails to start | Missing output folder boot loop; maintainer says root cause fixed |
| #85 | low | V4L2.py: _set_ctrl messes up menu or intmenu values | Report pinpoints faulty scaling line in V4L2 control code |
| #73 | low | [WRN] [NET] netcam_init_jpeg: no new pic, no signal rcvd | Motion warnings; maintainer committed change making log level followed |
| #42 | low | motioneye continuously fill journald | Journal flooding; maintainer changed default log level |
| #1862 + dup | high | camera name error | Numeric camera name design issue; duplicate of #1546, fixed by #2344 |
| #1713 | high | timelapse files have the wrong extension | AVI timelapse saved with mp4 extension; reconfirmed and flagged as bug |
| #1698 | high | Motioneye streaming not working on Firefox 75.0 | Firefox 75 streaming failure; fixed in motionEye 0.41, see #1428 |
| #1694 | high | Firefox 75/Chrome 81 cannot view cameras | Loading attribute misuse; maintainer links fixing commit |
| #1669 | high | thumbnails not removed. | Collaborator reproduced leftover thumbnails; fixed by PR #1828 |
| #1546 | high | Numeric camera names are not allowed | Collaborator agrees numeric names need validation or handling fix |
| #1517 | high | "Invalid configuration file line: motion_binary" when ever anything is | Maintainer links fixing commit |
| #1363 | high | Having non-ascii in root dir, file names or user password makes motion | Non-ascii paths fail; collaborator pinpoints code, fixed via PR#1377 |
| #1343 | high | Video not showing in motioneye frontend | Maintainer: problem fixed in 0.41rc1 |
| #1324 | high | Video not showing when chrome lazyload feature is enabled | Pinpoints motionEye JS 'loading' property clash with Chrome lazyload |
| #1321 | high | Encoding error about webhook request url | Webhook URL encoding error; fixed via PR#1362 |
| #1308 | high | Clean Cloud not working | Clean Cloud not really deleting; maintainer closed via #1368 |
| #1266 | high | From 0.40rc5-armhf to 0.40-armhf a lot of logs | Debug logging left in Docker image; collaborator fixed via PR#1267 |
| #1191 | high | 0.40rc4: streaming issue | Streaming defect fixed by linked commit in 0.40rc5 |
| #1177 | high | [0.40rc2] An error occurred. Refreshing is recommended... on adding ca | Add camera error fixed by linked commit |
| #1175 | high | [0.40rc1] An error occurred. Refreshing is recommended... on Apply but | Maintainer confirms options mapping defect; fixed in 0.40rc2 |
| #1001 | high | Timestamps | Timestamp defect; test image worked, fixed with next release |
| #973 | high | MotionEye Smart Mask set to 10 disables Mask | Maintainer confirms bug; fix commit linked |
| #914 | high | Dropbox filename truncation when using symlinks | Faulty path code pinpointed; maintainer links fixing commit |
| #895 | high | ERROR: failed to list mounted disks: 'unmatched' | Maintainer links fixing commit |
| #775 | high | Downloaded videos from Firefox are converted from .mp4 to .mp4.mpeg | Wrong mime type; maintainer says fixed via #785 |
| #740 | high | Cannot play mp4 recorded movies | Maintainer says fixed via #785 |
| #696 | high | Attached Pictures Time Span = 1 causes failures. | Maintainer links fixing commit |
| #685 | high | Can't access picture gallery after deleting some pictures via terminal | Maintainer links fixing commit; reporter confirms |
| #556 | high | embed url not working after ugrade to 0.36 | Maintainer confirms regression; commit fixes frame URL |
| #437 | high | mask creation and rotation of picture is inconsistent | Mask with rotation wrong; maintainer commit fixes it |
| #370 | high | Instructions for setting up a hub | Password with spaces failed; commit fixes it |
| #321 | high | thread-x.config file parsing fails if there are comments on the same l | Config parsing failure fixed by linked commit |
| #311 | high | First hit to /picture/1/current after a 15s period of inactivity resul | Empty first response; maintainer links fixing commit |
| #253 | high | RTSP camera test does not support Digest authentication | Pinpoints test_rtsp_url lacking Digest; commit fixes it |
| #249 | high | precompiled motion for RPi in wiki instructions doesn't work with late | Maintainer reproduced broken precompiled binary and rebuilt it |
| #237 | high | Cleanup issue with multiple cameras | Pinpoints cleanup_media defect; maintainer confirms and fixes |
| #224 | high | show frame changes (motion detect) | Frame changes on wrong camera; commit fixes it |
| #201 | high | Remote code execution | Remote code execution; maintainer commit fixes subprocess problems |
| #189 | high | No longer uploads to Google Drive | Special characters in password broke upload; commit fixes |
| #171 | high | Invalid client_id with Dropbox in motionEye 0.31.4 | Dropbox client_id placeholder unreplaced; report pinpoints the fault |
| #140 | high | Unable to add 10th camera to motioneye. | Tenth camera failure; linked pull request fixes it |
| #134 | high | Endless reboot loop if output folder was emptied | Reboot loop; maintainer says gone with next release |
| #106 | high | Webhook notifications failing with 400 | Maintainer confirms percent-escaped URL problem in webhooks |
| #89 | high | .AppleDouble directory errors | Maintainer agrees hidden folders should be ignored; PR submitted |
| #84 | high | Missing V4L2 controls | Pinpoints regex fault; maintainer loosened it |
| #83 | high | Add date to filename when saving to Google Drive | Uploaded files overwritten; maintainer links fixing commit |
| #80 | high | Displaying camera feeds on small screens | Maintainer confirms layout regression; fixed for 0.30 final |
| #69 | high | Send email only from specified cameras | Per-camera email problem fixed by maintainer, tested by users |
| #46 | high | Firefox on Linux: Picutre/Movies dialog | Firefox dialog breakage; maintainer mentions fix awaiting release |
| #30 | high | Error in service start | Maintainer: known bug, fixed in 0.28.2 |
| #29 | high | unknown configuration option: motion_control_localhost | Maintainer: known bug, fixed for 0.28.2 |
| #18 | high | Mr Dave's fork - motion not found on boot | Init script PATH fault; maintainer fixed the script |
| #16 | high | motioneye running out of memory (referring to bitbucket issue tracker) | Memory leak identified and fixed by maintainer in 0.28.2 |
| #12 | high | delete of /var/lib/motioneye | Root media directory removed; maintainer committed sentinel file fix |
| #7 | high | meyectl relayevent: error: unrecognized arguments: -b | Maintainer confirms special case; fixed for 0.27.2 |
| #2 | high | Ip Camera broken pipe | Maintainer identifies motionEye bug after first apply, recently fixed |

## `external bug` (18, low 14)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1907 | low | arch linux pycurl undefined symbol | Arch Python update broke pycurl; packaging workaround in AUR |
| #1641 | low | “Streaming image re-sizing” parameter and/or “Movie Quality” cause unp | Reporter traces unplayable files to Motion/ffmpeg H264 profile choice |
| #1351 | low | Camera not properly recognised on Raspbian Buster | Purple cast from Pi firmware AWB change; known problem |
| #1259 | low | netcam_highres  for manual screenshot | Low-res manual snapshots with netcam_highres; filed at Motion |
| #948 | low | motion detection | Reporter says issue is on Motion side, not motionEye |
| #930 | low | h264_omx has been blacklisted using codec libx264 | Codec blacklisted by Motion/ffmpeg build; users directed to Motion |
| #807 | low | Issue with Pillow-5.0.0 when installing in Raspbian | Maintainer calls it a Pillow issue, not motionEye |
| #525 | low | Cannot Capture Video When Motion Is Detected. | Motion version lacks mp4 support; reporter upgrades Motion |
| #426 | low | Unable to authorize rtsp stream with Amcrest | Reporter says not motionEye; moved to Motion project |
| #168 | low | motion log many warnings/errors | Log noise from Motion; gone with recent Motion versions |
| #105 | low | High CPU Utilisation - motion on RPi 2B | Reporter blames Motion or Ubuntu dependency for CPU use |
| #82 | low | Reconnect for RTSP | RTSP reconnect failure resolved by switching Motion binary |
| #39 | low | web video flash/jump fast | Flashing feeds gone after Firefox upgrade; browser implied, not confirmed |
| #21 | low | Chrome doesn't propose to save login/password after login | Chrome password prompt worked after Chrome update |
| #1552 | high | 0% GPU usage | Contributor attributes it to Motion; report it there |
| #1357 | high | Auto Brightness never settles to a stable state - Raspbian Buster, NOI | Reporter attributes auto brightness oscillation to Motion |
| #937 | high | [Moved in motion forum (759)]Can add camera but can't read rtsp in mot | RTSP problem moved to the Motion repo as an issue |
| #469 + dup | high | motion: [1:ml1] [ERR] [ALL] init_camera_type: Unable to determine came | Motion defect already logged; patch going into Motion; reporter says duplicate |

## `feature` (62, low 18)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1813 | low | Setting Long Shutter Time / Low Shutter Speed | Asks for longer shutter than currently supported |
| #1792 | low | Execute  all cameras snapshots when one sees motion. | Wants one camera's motion to trigger other cameras' snapshots |
| #1693 | low | gpg/gpg encryption for emails | Requests GPG email encryption; own-script workaround suggested |
| #1657 + dup | low | Feature request: Delete button in play mode | Requests delete button in player; also requested in #1425 |
| #1633 | low | replay | Asks for on-demand replay from seconds ago; unanswered |
| #1526 | low | Video streaming using decoder | Asks for H264 streaming using new Motion capability |
| #1507 | low | [Feature Request] Prebuilt image for embedded x86 systems (#2) | Requests x86 image; redirected to motionEyeOS project |
| #1241 | low | Feature Request: Visually Indicate when Motion Detection is Enabled | Requested indicator; maintainer says frame turns red on motion |
| #1112 | low | Motioneye with Sony PS3 eye camera with microphone - I would like to a | Wants automatic sound recording; reporter gave up |
| #719 | low | Intergrade with Discord webhooks | Asks about Discord webhook integration; no comments |
| #699 | low | latest motion screen: all pictures | Wants quick view of latest motion pictures; scripts suggested |
| #572 | low | Play video directly instead of needing to download | Requests playing videos in browser without download |
| #545 | low | Feature/Request: Two Networkinterface Support | Requests two network interface support; motionEyeOS context |
| #506 | low | AUDIO+VIDEO save in motioneye | Asks for saving audio with video; only script workarounds |
| #486 | low | Request: FTP upload scheduled and motion images | Requests scheduled FTP uploads; reposted to motionEyeOS repo |
| #456 | low | Using IP camera aux stream as motion detection & preview | Dual stream request; collaborator shows existing extra option workaround |
| #392 | low | Storage Device | Requests SSH or WebDAV storage; only SMB option mentioned |
| #56 | low | webhook on the end of event | Webhook request; partly already supported, new webhook added |
| #1923 | high | Create album per day when uploading to photos | Requests per-day albums for Google Photos upload |
| #1904 | high | Buttons for customs URLs | Requests custom URL buttons on camera image |
| #1841 | high | Motion Timeline | Requests motion timeline across cameras |
| #1838 | high | Detect camera dropping offline | Wants notification when camera goes offline |
| #1836 | high | Feature request: image interval time slots | Feature request for image interval time slots |
| #1794 | high | Measuring Speed | Asks for vehicle speed measurement and overlay |
| #1763 | high | Feature Request - batch configuration of cameras / system | Feature request for batch configuration of cameras |
| #1762 | high | Feature  suggestion: view last n seconds of stream on the fly | Requests viewing last seconds of stream on the fly |
| #1742 | high | Option to delete files when drive gets above certain percent full. | Requests deleting oldest files when drive passes a threshold |
| #1707 | high | Motion detection settings test | Proposes testing motion settings against captured media with feedback |
| #1677 | high | Feature request: Motion mask per time span | Feature request for time-based motion masks; cron workaround offered |
| #1665 | high | Motioneye Server use GPU HW Acceleration | Requests GPU acceleration in docker image; merge request invited |
| #1626 | high | Cycling the videos of the cameras (full screen) - one per time | Requests cycling full screen camera view |
| #1621 | high | Ability to add seperate PIR sensor for triggering? | Requests separate PIR sensor triggering |
| #1566 | high | Add functionality to web API | Requests new web API functionality to run scripts |
| #1539 | high | Proposal: If the Mobile phone is in the WIFI Network then Motion Detec | Proposes disabling recording when phone is on wifi |
| #1323 | high | [FEATURE REQUEST/SECURITY ISSUE] Allow to change admin username | Requests changeable admin username; maintainer declined |
| #1319 | high | [FEATURE REQUEST] Custom settings based based on ip range | Requests settings per IP range or user; declined |
| #1212 | high | [Feature] Google Photo upload | Requests new Google Photos upload service; done via PR |
| #1195 | high | Please add support for new config options | Requests support for new Motion options; implemented via PR |
| #1193 | high | Support for new mask option | Requests privacy mask support; implemented via PR |
| #1059 | high | Feature Request: Fetch status from meyectl | Feature request for status command in meyectl |
| #945 | high | Option to stream to youtube livestreaming channel | Requests YouTube live streaming option |
| #836 | high | Feature request: sound | Requests sound recording; needs Motion support first |
| #684 | high | Order cameras by groups | Requests camera groups; maintainer has no plans |
| #606 | high | Support for SMS Activate/Deactivate! | Requests SMS activation; maintainer declined to implement |
| #431 | high | mjpg-streamer support | Requests mjpg-streamer support; maintainer declined |
| #379 | high | Feature Request:: Option to turn off the Camera instead of deleting | Requests option to disable camera without deleting |
| #366 | high | Feature Request: Notification if camera is lost | Requests notification when camera is lost; users share scripts |
| #364 | high | Upload to S3 | Asks for S3 upload support |
| #355 | high | Translation | Asks for multilanguage translation; maintainer has no plans |
| #350 | high | Time based switching between motion and full records | Asks for time-based switch between motion and continuous recording |
| #324 | high | [feature-request] Display Disk Space Available / Used | Feature request to display disk space usage |
| #245 | high | Feature request | Requests editing camera URL in UI; maintainer declines |
| #217 | high | Feature request: pan-tilt control | Feature request for pan-tilt control |
| #188 | high | support for rtmp | Asks for RTMP support; Motion lacks it |
| #178 | high | feature-request: show video in html5-browser - expand "run a command" | Feature request for browser video playback; later implemented |
| #174 | high | Saving to animated GIFs for email notifications | Requests animated GIFs for notifications; maintainer declines |
| #115 | high | Ability to play recorded videos in browser | Requests browser video playback; implemented |
| #102 | high | h264 encoding and viewing video in interface | Asks h264 in-browser playback; mp4 container support coming |
| #94 | high | Feature request: ability to take snapshots from webui | Feature request for manual snapshots; now exists |
| #59 | high | Motion graph | Requests motion graph; closed as out of scope |
| #50 | high | Mask | Asks for mask file support; added in 0.34 |
| #49 + dup | high | Service to turn motion detection on and off for all cameras. | Requests service toggling motion detection; closed as duplicate |

## `enhancement` (50, low 20)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1840 | low | Capture Mode for Still Images and Recording Mode for Movies share the | Asks to separate still and movie capture modes |
| #1779 | low | Red frame while recording | Wants red recording frame when triggered by webcontrol |
| #1696 + dup | low | Python2.7 EOL'ed, Ubuntu 20.04 deprecates it | Python 2 EOL migration; already tracked in #1572 and others |
| #1688 | low | [Suggestion] Delayed Motion event saving/transfer | Suggests delaying event processing to keep framerate during motion |
| #1640 | low | Python3 support? | Asks to port motionEye to Python 3 |
| #1605 | low | Slow load times when loading movies for a camera | Asks to improve slow movie list loading |
| #1423 | low | Docker Compose version 3.5 | Docker compose file updated to version 3.5 by commit |
| #1372 | low | Support for despeckle filter needed | Despeckle request; reporter found it already implemented |
| #1299 | low | 'Failed to load picture list' error when number of images is large | Large picture list timeout; media listing performance later improved |
| #1274 | low | Predefined retention rules | More retention choices requested; custom option already exists |
| #864 | low | docker mmal camera support | MMAL support added to Docker image by merged PR |
| #763 | low | Disable thumb creation | Wants thumbnail creation disabled; currently hard-wired, workaround shared |
| #605 | low | Motion trigger never ending | Continuous recording prevents motion events ending; no simple solution |
| #494 | low | cross domain not allow | CORS blocks embedding streams; collaborator discusses adding header |
| #378 | low | Base Path for both Reverse Proxy and Direct Access? | Direct and proxy access; base_path removed for relative paths |
| #344 | low | smart mask not working | Maintainer adds UI support for smart mask and debug options |
| #283 | low | Change request: change the direction of the scroll arrows when looking | Asks to reverse browsing arrows; commit implements it |
| #276 | low | Webhook connecting the openHAB | Commit adds option allowing self-signed HTTPS webhooks |
| #121 | low | Passwords dumped into /data/etc/motion.conf in plain txt? | Complaint about plain-text passwords; maintainer rejects as non-issue |
| #54 | low | Variables for notifications | Asks variables passed to existing notifications; conversion specifier provided |
| #1819 | high | MotionEye runs in docker as user root. | Proposes running Docker container as non-root |
| #1817 | high | UI suggestions | Ease-of-use suggestions for existing UI |
| #1798 | high | Save Run a Command text when disabled | Wants Run a Command text kept when disabled |
| #1773 | high | Webinterface Bootstrap | Proposes Bootstrap frontend to improve mobile UI |
| #1766 | high | Amount of Action Buttons | Asks to raise action button limit; later implemented by #2903 |
| #1761 | high | Request for new functions in Movies recorded list | Asks duration and multiselect delete in existing movies list |
| #1672 | high | [Feature Request] Allow full use of strftime syntax | Asks fuller strftime support in existing file name patterns |
| #1651 | high | Google Drive Permission Scopes | Asks narrower Google Drive permission scopes for existing upload |
| #1425 | high | Should have an option to "Delete" when viewing a saved image/video | Delete button in single view; implemented via PR#1833 |
| #1409 | high | Add "delete" button in modal-buttons-container | Delete button in media modal; implemented via PR#1833 |
| #1313 | high | Improvement: Display slider value when hovering the cursor | Slider value tooltip on hover; implemented via PR#1314 |
| #1309 | high | Feature Request: Add a delete option on the media playback popup | Delete option in media popup; implemented via PR#1833 |
| #1178 | high | get camera id from config file not from camera config file name | Asks for different camera id source; maintainer declined |
| #918 | high | Feature Request: More Action Buttons | Asks for more than eight action buttons |
| #799 | high | Edit despeckle filter | Asks UI to display customized despeckle filter |
| #797 | high | Feature request: advanced mask file | Requests improving the existing mask file dialog |
| #677 | high | Do not set text_double on for cams 800x600 and smaller | Requests text_double behaviour change; implemented by commit |
| #674 | high | Better mail sending (use sendmail, send camera lost warnings, be able | Requests improvements to existing mail notifications |
| #613 | high | [Feature request] Special frame for action buttons | Requests more action buttons space; fixed by PR #2903 |
| #550 | high | Suggestion for "Delete" | Suggests delete button in preview; closed via PR #1833 |
| #436 | high | Max File Upload Size (128MB). Possible to increase? | Asks to raise upload size limit; commit raises to 1GB |
| #269 | high | 1080p support | Asks to add 1080p to resolution options; now available |
| #254 | high | Can the new resolutions from raspberry camera be added to motioneye gu | Asks for more resolutions in GUI; commits add them |
| #131 | high | Make LIST_MEDIA_TIMEOUT Configurable for Email Notifications | Patch making timeout configurable; maintainer added the setting |
| #130 | high | Performance improvement of list_media | Performance patch for list_media |
| #129 | high | Performance improvement of _list_media_files | Performance patch merged by maintainer |
| #111 | high | Use "SMTP Account" or add separate "From email" field to "Send An Emai | Asks configurable From address for emails; added in 0.31 |
| #22 | high | Add session cookie to maintain authorization | Requests remembered login; closed since cookie now stores hash |
| #19 | high | lightswitch settings enhancement request | Asks to make lightswitch setting adjustable |
| #15 | high | Allow more motion detection tuning options | Asks more detection tuning options; added in 0.34 |

## `documentation` (26, low 5)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1737 | low | I just published a video tutorial and article about the MotionEye | Offers tutorial links for README or wiki; no problem reported |
| #1730 | low | Incompatibility with Fedora 31 | Fedora install instructions outdated regarding Python 2 versus 3 |
| #861 | low | Documentation: sphinx | Proposes generated Sphinx docs; maintainer declines |
| #635 | low | Raspbian (based on Debian Stretch) unresolved dependencies | Wiki install steps list packages unavailable on Stretch |
| #241 | low | motion-mrdave-raspbian compiled against libraries not found in Raspbia | Missing dependency; maintainer added libx264-142 to wiki |
| #1839 | high | Document variables accessible for webhook in the mouseover help text | Asks to document webhook variables in help text |
| #1821 | high | Update Archlinux installation instructions to include AUR package | Asks wiki to list Arch AUR package |
| #1770 | high | Add curl to installation packages for Raspberry Pi | Asks to add curl to the Raspberry Pi wiki install instructions |
| #1650 | high | Clarify nginx configuration in wiki | Asks wiki note about nginx proxy_pass trailing slash |
| #1562 | high | Debian/Raspbian install instructions can be simplified | Wiki install instructions could be simplified |
| #1455 | high | Bad wiki for Docker ports | Docker wiki port syntax wrong; wiki fixed |
| #1345 | high | Update Docker build instructions | Docker wiki missing streaming ports; wiki updated |
| #1342 | high | Incorrect help text for smart mask sluggishness | Wrong help text in UI; maintainer fixed description |
| #1320 | high | Fix installation guide for Archlinux | Arch install guide correction; wiki updated |
| #1278 | high | Wiki installation instruction | Wiki install steps missing libraries; maintainer updated |
| #1171 | high | Install On Fedora - wiki | Fedora wiki instructions wrong; maintainer updated them |
| #1115 | high | Wiki minor tweak | Wiki tweak requested; maintainer added a note |
| #1069 | high | motioneye.conf.sample: No such file or directory during copy | Wrong install path in wiki; documentation updated |
| #1041 | high | Wiki: Installation Instruction Updates for Linux Mint 19 | Wiki installation notes shared for Linux Mint |
| #1027 | high | Ubuntu install instructions need updated. | Ubuntu instructions lack needed repository step |
| #839 | high | Installation instructions incomplete | Wiki missing dependencies; updated |
| #835 | high | setuptools prerequisite is missing | Wiki missing setuptools prerequisite; added |
| #786 | high | Arch Linux ARMv7 requires lsb-release | Asks wiki update for Arch requirement; done |
| #633 | high | The wiki reference the deb on github while motion repo is newer | Wiki outdated about Motion package; wiki page updated |
| #488 | high | Run motion outside of Motioneye | Requests docs on running Motion separately; wiki page written |
| #60 | high | wiki suggestion | Wiki missing autoconf package; maintainer updated it |

## `meta` (3, low 1)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1785 | low | MotionEYE needs a webpage, changelog and update methods | Asks project for webpage, changelog and update methods |
| #275 | high | Contributing | Asks about contributions and project build process |
| #272 | high | Time for a user forum? | Proposes user forum and issue labels for project |

## `CI/CD` (3, low 3)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1818 | low | Dockerfile does not build | Dockerfile build broken; fixed by merged PR #1822 |
| #1809 | low | ARM64 Docker hub builds | Requests ARM64 Docker Hub builds; Travis build pipeline discussion |
| #1749 | low | Manifest for ccrisan/motioneye:latest not found | Docker image latest tag missing; packaging tag scheme discussed |

## `invalid` (20, low 5)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1652 | low | Warning | Abusive rant warning users; no usable question or report |
| #1501 | low | Problems with installation on step4: motioneye.conf doesn’t exist | Short title, no body; reporter closed with just 'closed' |
| #955 | low | . | Title is a dot, empty body; comments discuss video pauses |
| #377 | low | Free Human Body recognition | Shares a script; no question or problem reported |
| #362 | low | Sharing a small script for hangout alerts | Shares a script; no question or problem |
| #1735 | high | Dvr | Title Dvr, empty body; commenter asks what the question is |
| #1578 | high | Way to open full screen view in new window? | Short title only, no body and no comments |
| #1564 | high | DELETED | Deleted by author; posted in wrong place |
| #1545 | high | - | Title and body are just a dash |
| #1525 | high | 1072av | Meaningless title, no body, no comments |
| #1468 | high | Rasbian install problem | Short title, no body, no comments |
| #1464 | high | rtorrent crashes on starting | rtorrent crash opened here by mistake |
| #1462 | high | Curl issue? | rtorrent problem unrelated to motionEye, posted by mistake |
| #1126 | high | Adding Network cam No picture | Short title, meaningless body, no comments |
| #1039 | high | MotionEyeOS wont boot | Body deleted, no comments |
| #889 | high | No video streaming options | Short title, no body, no comments |
| #770 | high | Can't modify sliders from mobile | Short title, no body, no comments |
| #702 | high | Error "failed to call webhook" | Body is only 'done plz delete'; nothing to read |
| #318 | high | Boot Log | Just a boot log; maintainer asks what it is about |
| #234 | high | Extermal trr | Meaningless title, no body, no comments |

## `troubleshooting` (201, low 74)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1941 + dup | low | "unable to open video device" when having 2 cameras | Device open error; author only comments duplicate, no cause given |
| #1891 | low | Camera not write data to folder or GoogleDisk | Config conflicts noted but unresolved; closed for no followup |
| #1882 | low | Applying settings triggers false alarm | False alarm on apply; bulk closed, nothing confirmed |
| #1866 | low | Can not connect to Motioneye web interface when installed on Raspberry | Install step possibly wrong; no confirmed resolution |
| #1835 | low | Video is blurry or showing rainbow colors, what could be the issue? | Rainbow images; only guesses about packets or camera |
| #1815 | low | Disabled password protection, but it still asks for one | Embed URL still asks password; no answer, bulk closed |
| #1814 | low | Camera drops out and stops working constantly | Camera drops; reporter suspects Samba storage, not established |
| #1803 | low | Failed Authentication when adding Network Camera | Foscam authentication failure; no comments, bulk closed |
| #1802 | low | Failed to upload Media file | SFTP upload error; thread drifted, no cause shown |
| #1780 | low | Installing motioneye on openSUSE Tumbleweed | openSUSE install failure without python2 pycurl; no reply |
| #1771 | low | Cannot save files to extern HDD | Cannot save to external HDD; no reply, bulk closed |
| #1769 | low | Display same picture for 2 differents camera in Gui but Record is OK | Same picture on two cameras; port hint offered, reporter never confirmed |
| #1768 | low | Laggy video on lower output quality and no AMD VCE | Laggy video at lower quality; no comments, no cause |
| #1747 | low | Delay in RTSP feed (40-60 seconds) | RTSP delay; users share tips, no definite cause |
| #1736 | low | Rotating a fast network camera steam doesn't rotate the resolution wit | Rotated fast network stream keeps landscape; unconfirmed, no diagnosis |
| #1717 | low | Cannot get both MotionEye and Lovelace streaming... | ESP32 Home Assistant setup struggle; closed by reporter without explanation |
| #1716 | low | motioneye not saving photos or videos | Not saving media; permissions suspected, never confirmed |
| #1685 | low | USB Webcam not showing video in webgui | Webcam shows no video; reporter's case unresolved, other user's docker fix |
| #1683 | low | Blocked by CORS | CORS block on stream; closed by reporter with no comments |
| #1670 | low | SV3C Model SV-B06W-1080P-HX-2 Not Working | Camera fails; listen address change helped, cause unclear, reporter closed |
| #1663 | low | pushover.py script working but not triggered by Motion Detection - Run | Script not triggered by motion; closed by reporter, no cause |
| #1646 | low | Remote motioneEye Camera - authentication failed | Authentication failure; wifi answer doesn't fit, another user still affected |
| #1638 | low | Too much upload traffic with motion / motioneye | High traffic report; no cause established |
| #1620 | low | CPU usage | CPU load and idle GPU; never resolved |
| #1606 | low | Can't get RTSP stream | RTSP stream failure; only a generic workaround from another user |
| #1604 | low | usb camera not opened | motionEyeOS camera failure; reporter still stuck, no resolution |
| #1600 | low | Q:  Is it a bug or a feature? | Remote camera motion frame not shown; no answer |
| #1581 | low | Invalid configuration file line: motion_binary and I cannot access the | Invalid config line; reinstalled, cause never established |
| #1575 | low | Poor Performance on A RPI3 | Low FPS on RPi3; unanswered, hardware or config unknown |
| #1553 | low | Optimized for the Pi4? | Poor multi-webcam performance on Pi4; no answer |
| #1551 | low | A lot of warning/errors at /var/log/messages etc at Raspberry Pi 2B+ w | Log warnings; closed by reporter with no explanation |
| #1536 | low | Grey image after upgrade | Grey image after upgrade; migration explained, camera failure unresolved |
| #1511 + dup | low | After update to debian 10 python errors | Python errors after upgrade; duplicate of #1494, no answer |
| #1426 | low | Multiple RPI's with MotionEyeOs not able to remotely connect to eachot | Remote camera connect worked in another browser; cause unknown |
| #1303 | low | Camera device/type changed following power cut | Power cut likely corrupted OS; reinstall suggested, not confirmed |
| #1218 | low | Manual install doesn't upgrade anymore | Upgrade problem resolved long ago; reporter gives no cause |
| #1216 | low | device busy | USB camera device error; reporter closed without stated cause |
| #1201 | low | Streaming Port Change Kills Stream | Not reproducible; reporter closed after manual config edits, cause unclear |
| #1179 | low | ERROR: the maximum number of tasks (100) has been reached ( on a RPI3) | Upload task limit error; visible comments give no diagnosis |
| #1120 | low | Pi Cam working but not showing on WebUI | Copying motion.conf and rebooting fixed it; cause unclear |
| #1090 + dup | low | "Name or service not known" | Empty body; author says probably duplicate of #1088 |
| #1088 | low | Motioneye is not recognizing PS3 Eye camera | Hostname revert helped reporter; no real diagnosis, ancient close |
| #1026 | low | Can not record Videos on RTSP Stream... | RTSP recording failure; varied workarounds, no established cause |
| #989 | low | motioneye.service failed to start | Service failed; reporter resolved without stating cause |
| #981 | low | Can't Add a Camera | Add camera blocked; assorted workarounds, no established cause |
| #965 | low | Camera Resolution and Video rotation ignored. | Back to work after upgrade; nobody knew the cause |
| #938 | low | pip install was interrupted | Bad pip archive, cause unknown; suggested fix never confirmed |
| #906 | low | NOT CLOSED --> Motion not being detected in motioneye 0.39.1 motion 4. | Filename pattern suspected; maintainer says should work, no diagnosis |
| #855 | low | Unable to install MotionEye on Raspbian 2018-03-13 | Unmet dependency install failure; no clear resolution, stale close |
| #745 | low | No MMAL camera detected | No MMAL camera on Arch; ending not visible in comments |
| #744 | low | Action button 500 error | Action button 500 error; visible comments show no cause |
| #710 | low | USB Wlan Sticks dont work on ZeroW | motionEyeOS USB WLAN on ZeroW; no comments, no answer |
| #680 | low | install motioneye on Raspbian stretch give some errors | Dependency errors on Stretch; never resolved for reporter, stale close |
| #649 | low | Hard refresh needed when changing some settings (0.37) | Hard refresh fixed it; auth change possibly related, unconfirmed |
| #566 | low | remember me not working with embed url | Maintainer would look; closed as stale, feature later removed |
| #524 | low | Error capturing first image - after several hours of operation | Camera becomes unavailable; maintainer points to Motion, no cause found |
| #497 | low | "no camera" found RPi Zero W | No camera found on Pi Zero W; later works, cause unknown |
| #474 | low | No motion detected | No motion on motionEyeOS; moved elsewhere without diagnosis |
| #453 | low | Raspberry Pi Spy Cam not working with MotionEye? | Spy camera add error; long thread, no established cause |
| #433 | low | Problem adding Remote motionEye Camera | Remote camera spins; logs show no issue, maybe bandwidth |
| #429 | low | Motion Detection on 1 camera; not another | Recreating the camera fixed detection; cause not identified |
| #422 | low | endless login when adding a camera | Endless login adding camera; suggestions only, no confirmed cause |
| #398 | low | bcm2835-v4l2 error 0 waiting for frame completion | Random bcm2835-v4l2 frame errors; power suspected, nothing established |
| #389 | low | Scheduler Problem | Scheduler caching problem in Edge; maintainer could not understand it |
| #386 | low | DropBox | Dropbox config questions and empty json; old, stale close |
| #384 | low | Duplicate cameras? Same video in different cameras | Deleting and re-adding cameras fixed; likely port glitch in config |
| #360 | low | Wireless issues motion eye | WiFi problem gone after reburning SD card; cause unclear |
| #260 | low | CSI camera not recognised, unable to load Module bcm2835-v412. | CSI camera not recognised; no diagnosis in given comments |
| #158 | low | i cant use upload to service HELP!!! | Maintainer made upload fixes, asked to retest; never confirmed (agent: bug, changed in review) |
| #153 | low | Exposure hanging issue with Raspberry Cam | Problems vanished after moving Pi; WLAN suspected, cause unclear |
| #150 | low | Video format | Unplayable avi files; cause unknown, codec option suggested |
| #135 | low | 0.31 stopped sending pictures. | Re-adding cameras fixed it; media timeout explanation not confirmed |
| #114 | low | Gray screen | Maintainer suspects buggy camera driver; only a guess (agent: external bug, changed in review) |
| #99 | low | No previws pics? | Missing thumbnails; no cause visible, Wheezy unsupported by maintainer |
| #1926 | high | Severe video delay | Growing stream delay; no cause established |
| #1903 | high | I can not run a command when motion is detected | Command not run on motion; bulk closed, no diagnosis |
| #1896 | high | Motion Eye cannot detect my camera | Camera undetected, odd behaviour, cause never found |
| #1890 | high | Cannot add network camera | Cannot add camera in Docker; closed for no followup |
| #1888 | high | ccrisan/motioneye:master-armhf constantly restarting .... | Container restart loop; closed for no followup |
| #1886 | high | Motion detection trigger even though it is turned off | Detection triggers when off; no comments, no cause |
| #1885 | high | How i can fix "Unable to open video device" | Video device error; closed for no followup, undiagnosed |
| #1883 | high | Camera only works if i add 2 other broken ones | Odd camera behaviour; bulk closed with no comments |
| #1881 | high | failed to register layer: error creating overlay mount to /var/lib/doc | Docker overlay error; no answer, bulk closed |
| #1880 | high | Can't play H265 | H265 recordings unplayable; collaborator does not know cause |
| #1877 | high | Google Drive auth key needs regenerating everytime motioneye addon is | Drive key lost on addon restart; no diagnosis |
| #1873 | high | issue with docker compose and missing config data | Config directory error in Docker; never solved |
| #1865 | high | Watchdog Timeout / Motion Stream Server Port Redundancy | Watchdog timeout after update; no comments or diagnosis |
| #1832 | high | Not working RTSP on raspberry pi 4 (Deb 10) | RTSP fails on Pi 4; suggestions only, no resolution |
| #1830 | high | Motion won't create more than one video | Only one video created; others agree, no cause found |
| #1826 | high | Web Interface has no options | UI dead, Opera worked, original cause unexplained |
| #1823 | high | Gdrive file upload | Upload config lost on addon restart; no answer |
| #1807 | high | Can't disable motion detection in docker | Connection refused in Docker; stale close, no solution |
| #1806 | high | CPU utilization | CPU grows over time; no comments or cause |
| #1804 | high | H264/V4L2M2M turns video green | Green video with V4L2M2M; no answer |
| #1800 | high | live stream freeze | Stream freezes in Home Assistant; no answer |
| #1793 | high | Failed to upgrade to 20200606 | Firmware upgrade traceback; no answer, bulk closed |
| #1790 | high | unable to open video device and  connection to camera lost | Webcams fail; suggestion did not help, unresolved |
| #1786 | high | streaming url not working in VLC on pi 4 | Stream shows no picture in VLC; no answer |
| #1784 | high | Saved movies have a low frame rate | Low frame rate on Pi Zero; no comments |
| #1767 | high | Frame rate drops to 0.0.fps and recording stops.. | Frame rate drops to zero; no comments, no diagnosis |
| #1758 | high | Wrong color | Pink image after moving SD card; long thread, no established cause |
| #1755 | high | MotionEye does not show image but records ok | No image with 401 errors; no solution found |
| #1753 | high | Daytime / nightime transitions go to white or black screen. | Day/night transition image problem; reporter moved to forum, no cause |
| #1752 | high | rtsp client error: timeout connecting to rtsp netcam | RTSP timeout under docker only; cause never established |
| #1740 | high | Can't watch stream on web | Stream stopped showing; closed by reporter with no comments |
| #1739 | high | Motioneye on Raspbian buster: HW acceleration not working? | Hardware acceleration apparently not working; no response, no diagnosis |
| #1734 | high | motioneye in docker, raspi camera via rtsp://, does not work | RTSP in docker refused; no answer, no cause |
| #1733 | high | Test e-mail sends, Motion e-mail does not | Motion email not sent; no comments, no diagnosis |
| #1731 | high | Full screen view doesn't work all the times anymore | Fullscreen problem went away by itself; cause only guessed |
| #1727 | high | motion_webcontrol (:7999) does not seems to work with USB camera | Webcontrol fails for USB camera; no comments, no diagnosis |
| #1726 | high | Raspberry (3&4): automatic exposure not working on resolutions > 800x6 | Auto exposure fails at higher resolutions; no comments, no cause |
| #1725 | high | Double Upload | Double upload to Google Drive; no comments, no diagnosis |
| #1715 | high | Backup option no longer works in dev-amd64 | Backup hangs on dev image; no comments, no diagnosis |
| #1710 | high | Once Fast Network Camera is off, the camera is unable to open | Camera fails after disabling fast network mode; no diagnosis |
| #1703 | high | Docker: OCI runtime create failed armhf (pi4) | Docker OCI runtime failure on armhf; no answer |
| #1702 | high | Stream working but recordings are "unable to open video device" | Recordings show unable to open device; no comments, no diagnosis |
| #1700 | high | FTP Fails to upload data whilst Test succeeds | FTP test passes but uploads fail; no comments, no diagnosis |
| #1695 | high | gray box instead of the video (mjpg client timed out) | Gray box with mjpg timeout; no comments, no diagnosis |
| #1692 | high | motioneye is not started | Service fails after update; closed by reporter, no cause given |
| #1676 | high | Camera turns off after extended use | Camera stops after extended use; no comments, no cause |
| #1675 | high | Unable to add rtsp camera - worked previously | Rebooting camera fixed it; reason unknown |
| #1674 | high | usb webcam not detected by motion eye os | USB webcam not detected; no comments, no diagnosis |
| #1668 | high | Unable to add remote motionEye Camera - RPi4B with Raspbian Buster | Remote camera error; another user's disk hint unconfirmed by reporter |
| #1662 | high | Artifacts | Artifacts fixed themselves, reporter unsure why; no diagnosis |
| #1659 | high | Google drive upload error | Google Drive upload fails after restart; no resolution |
| #1653 | high | Maximum Movie Length not working? | Recording stops after maximum length; no comments, no diagnosis |
| #1642 | high | After selecting "Fast Network Camera" to the ON position: get gray pix | Told to try prerelease; outcome never reported |
| #1637 | high | Stream puzzles when adding a NAS with PS3Eyecam | Stream corruption report; no comments, stale close |
| #1636 | high | No 'Motion'-camera stream in 'MotionEye' | Connection problem; no comments, stale close |
| #1623 | high | Motion.conf blank | Config went blank mysteriously; not reproducible, cause unknown |
| #1618 | high | error setting working schedule | Schedule error; no follow-up, cause unknown |
| #1609 | high | Dual cameras + Equal resolutions results in no stream | Logs requested, none given; cause never established |
| #1595 | high | Motioneye not controlling Motion (0.42 - 4.2.2) | Device busy errors; closed by reporter with no answer |
| #1594 | high | unable to open camera (grey) in OS and raspbian builds -  noob | Camera won't open; no comments, stale close |
| #1585 | high | MotionEye stops working after 24hs on Raspberry Pi 3 B+ with 3 cameras | Stops after 24 hours; closed by reporter, no cause |
| #1582 | high | motioneye on raspberry pi with 5 cams - cameras swap positions after r | Cameras swap after reboot; no comments, stale close |
| #1573 | high | "Unable to locate package libmariadb3" when installing on Raspbian | Package not found during install; no comments, stale close |
| #1556 | high | Issue with clean installation, | Traceback on clean install; no comments, stale close |
| #1555 | high | Video becomes black and white after IR cut-off filter is toggled. | Intermittent black and white video; no comments, no cause |
| #1540 | high | Recorded videos always stutter after a few seconds | Stuttering recordings; cause never established, reporter switched software |
| #1538 | high | Motioneye don't start after installation on Raspbian Buster | Would not start; reporter made it work, cause unstated |
| #1535 | high | Movie recordings wont playback on mobile | Mobile playback failure; no comments, stale close |
| #1514 | high | Error: "python setup.py egg_info" | pycurl install error; closed by reporter, no answer |
| #1512 | high | Interesting Network Interference | Network issue; closed by reporter with no comments |
| #1506 | high | "Connection to Camera Lost", Gray Video | Connection lost on webcam; no diagnosis, stale close |
| #1495 | high | No image nor video raspberry zero w | Pi camera no image; closed by reporter without any comments |
| #1472 | high | RPI3b+ Motioneye not starting - No module named motioneye | Module not found on start; no comments, closed by reporter |
| #1437 | high | Corrupt snapshot files, no clues in debug | Corrupt snapshots; closed by reporter with no diagnosis |
| #1431 | high | Upgrade from 0.39.3 to 0.40 fails | Upgrade failed; retrying worked, cause unknown |
| #1388 | high | RPi Buster - ModuleNotFoundError | ModuleNotFoundError never solved; reporter switched to diet-pi |
| #1385 | high | Multiple issues with 0.40 | Multiple camera problems, no reply, closed by reporter |
| #1341 | high | Motioneye network shares wont work on VMs | Network share and FTP failures on VMs; no diagnosis |
| #1294 | high | Problems in arm/disarm motion detection via motion Web API | Detection pause reverts; closed by reporter without explanation |
| #1279 | high | sv3c 1080p Cam setup as a webcam | No signal fixed by reinstall on newer Ubuntu; cause unknown |
| #1275 | high | Saved movies no longer being auto-deleted as per settings | Retention cleanup missing old files after reconfigure; cause never established |
| #1246 | high | Ubuntu to Windows File Storage (Videos clips) | Video writes to Windows share fail; no comments, cause unknown |
| #1237 | high | Migrate issue | Migration script syntax error; no resolution, closed years later |
| #1210 | high | jpgs being saved, stills are disabled, no movies being saved | Re-applying configuration fixed it; cause unknown |
| #1184 | high | Low CPU but low FPS on Raspberry Pi 3B | Low FPS report; no comments, no cause established |
| #1166 | high | Cant Check for update - "Apply modified Settings first" - OS 20180627 | Check update message persists after reimage; no answer given |
| #1136 | high | Green screen from RPi zero network cam stream | Green screen stream; stale close without a diagnosis |
| #1127 | high | adding network cam in hassio or linux mint give no picture | Network camera no picture; closed "fixed" with no cause |
| #1044 | high | MotionEye keeps restarting | Restarting and camera failures; no diagnosis visible, closed by member |
| #1022 | high | Timelapse movie could not be created | Timelapse failure; closed as stale without a diagnosis |
| #997 | high | Motioneye instable | Instability; hardware suspected, cause never established |
| #984 | high | [BUG] motion recording movies but striked camera logo in the UI instea | Stale close asking to retest; no cause established |
| #890 | high | Errors. | Remote camera error; no comments, closed without diagnosis |
| #882 | high | ImportError: No module named motioneye.meyectl | Clean OS reinstall fixed it; cause not established |
| #876 | high | `Active: failed` on new Install on Ubuntu | Service failure; reinstalling dependencies, cause never established |
| #874 | high | Viewing video thumbnails is very slow | Slow thumbnails report; no comments, no diagnosis |
| #847 | high | motion.conf | Motion disabled on new install; no resolution, stale close |
| #819 | high | Cleanup problem | Cleanup not working; later just worked, cause unknown |
| #801 | high | Motioneye won't start on Debian 9 | Service failure; no comments, no diagnosis |
| #784 | high | [Errno 13] Permission denied: '/home/pi/myNAS/Surveillance/Voordeur/.k | NAS permission error; reporter gave up, cause unknown |
| #759 | high | Problem with apply button | Apply error; no logs, closed for missing information |
| #750 | high | Motioneye causes rpi3 to hang following motion detection | Pi hang; moved to another machine, cause never found |
| #672 | high | Manual Snapshot not working | Snapshots began working after restarts; cause unknown |
| #528 | high | Green image after latest upgrades | Green image after upgrade; no comments, no diagnosis |
| #507 | high | Motioneye service not starting with fadora | Service fails on Fedora; no comments, cause unknown |
| #491 | high | Streaming a second camera kills all feeds | Reboot cleared feed failure; reporter does not know why |
| #483 | high | [local-ip] ERR_CONNECTION_REFUSED | Connection refused; full reinstall fixed it, cause unknown |
| #457 | high | Dropouts: No Camera graphic even with 100% framerate | Dropouts stopped after full reinstall; cause unknown |
| #390 | high | Unable to open video device | Reporter could not find root cause; restoring backup fixed |
| #376 | high | USB Camera - Unable to open video device on a grey screen | USB camera grey screen; closed for lack of activity |
| #343 | high | Hikvision network camera with raspberry pi b | RTSP camera problem, no comments, closed by reporter |
| #342 | high | WARNING: Connect error on fd 14: ECONNREFUSED | ECONNREFUSED after Motion upgrade; no cause established |
| #334 | high | ERROR: failed to set config for remote camera 1 | Remote camera error never diagnosed; closed as old |
| #328 | high | motioneye ffmpeg error on first start | ffmpeg errors reported; no comments or diagnosis |
| #322 | high | MotioneyeOS upload works - Raspbian and Motioneye does not | Gdrive upload fails on Raspbian; pycurl problem unresolved |
| #316 | high | Camera not detected | Camera not detected; closed for lack of feedback |
| #313 | high | motioneye on Ubuntu 16.04.1 running into install/launch problems | Install problem on Ubuntu; maintainer out of ideas |
| #303 | high | Advanced settings and its on but not showing. | Advanced settings missing; no comments, closed by reporter |
| #259 | high | Message: An error occurred. Refreshing is recommended. | Error resolved by itself; cause unknown |
| #248 | high | google drive error | Upload error gone after reboot; cause unknown |
| #162 | high | Extreme cpu usage on rpi3 | High CPU report; maintainer would look, no cause established |
| #149 | high | Video format | Unplayable avi files; no comments, closed by reporter |
| #138 | high | Running as normal user | Non-root start failure; never diagnosed, stale close |
| #112 | high | HTTP error 500 | Error 500 cleared by reboot; cause never established |
| #72 | high | Motioneye service stays stopping and starting | Service restart loop fixed by fresh install; cause only guessed |
| #28 | high | MotionEye always reboot | Reboot loop on motionEyeOS; reinstall worked, nobody knows why |
| #3 | high | failed to get motion detection status for camera with id | Fresh install resolved it; cause never established |

## `question` (473, low 97)

| Issue | Conf. | Title | Reason |
|---|---|---|---|
| #1919 | low | Using movie_extpipe_use/movie_extpipe | Usage question about movie_extpipe; long support thread, no defect |
| #1917 | low | Motioneye not running on RaspberryPi after minor edits to html templat | Custom build problem gone after using latest Docker image |
| #1884 | low | Distorted image with Sricam sp017 | Reporter says raising FPS seems to fix distortion |
| #1876 | low | IP camera address not editable in GUI? | Asks how to change camera IP; backup edit workaround given |
| #1870 | low | Streaming freezing every 2-3 days | Reporter moved it to motionEyeOS; wrong project |
| #1861 | low | MotionEye not creating log file | Logs go to journal under systemd; explained, wiki note suggested |
| #1796 | low | Hi CCrisan GoodJob on your Project.  Camera Question | Asks about offline Pi camera use; hints at feature |
| #1788 | low | PTZ Onvif | Asks how to configure PTZ ONVIF camera; no reply |
| #1765 | low | Deinterlacing | Asks whether deinterlacing is possible; closed by reporter unanswered |
| #1764 | low | Higher resolution for Pi HQ Camera | How to use higher resolution; collaborator explains stream and passthrough options |
| #1748 | low | MotionEye detects 3 non-existant cameras | Asks what the listed codec devices are; unanswered |
| #1724 | low | Still image is generated after notification is sent | Collaborator explains command runs at event start; capture mode setting matters |
| #1711 | low | Can't get snapshot url to work in octoprint. | Asks for snapshot URL without authentication; unanswered |
| #1682 | low | i5-6600T hwaccel help | Asks help configuring hardware acceleration; only a decoder hint given |
| #1673 | low | Incorrectly reported OS | OS shown comes from docker container; no defect established |
| #1666 | low | Motioneye Reboot Problem... | Start failure solved by installing missing pytz; others had corrupted config |
| #1648 | low | upgrade on raspbian stretch - problem | Upgrade issue; lost cameras explained by missed config migration instructions |
| #1647 | low | snapshot file name doesn't match video filename (motion detection) | Collaborator explains snapshot timing; no defect established |
| #1622 | low | reolink camera | Users fixed it by removing special characters from password |
| #1610 | low | MotionEyeOS doesn't start after a power cycle if network is down | motionEyeOS problem; reporter moved it to the motionEyeOS forum |
| #1608 | low | in-url rtsp stream authentication fails | RTSP credentials; users suggest URL format or separate fields |
| #1579 | low | Problem adding IP camera - Noob level | Noob asks how to add P2P IP camera; setup help |
| #1565 | low | Use DNS name for cameras? | How to use DNS names for cameras; unanswered |
| #1563 | low | Camera's always active | Asks how to keep camera off unless viewing; unanswered |
| #1548 | low | I want control PTZ through physical buttons/joystick/gamepad? | Asks if gamepad PTZ control is possible; speculative answer |
| #1530 | low | Recording in H.264/MPEG-4 AVC | Asks how to record with a smaller H.264 codec; unanswered |
| #1494 | low | after upgrade Debian 9 to 10 CURL_OPENSSL_3 error | OS upgrade broke pycurl; reinstalling pycurl via apt worked |
| #1448 | low | Motioneye continously storeing still images although not enabled ! | Leftover migrated config caused continuous stills; user side fix |
| #1446 | low | ONVIF support | ONVIF camera working after finding correct RTSP URL and port |
| #1429 | low | FPS really slow | Slow FPS attributed by reporter to poor wifi |
| #1421 | low | Unable to open video device | Stale camera config files removed by user; fixed the problem |
| #1407 | low | Secondary feed from Raspberry Pi camera | Asks about raw secondary camera feed into Motion; YUV suggested |
| #1398 | low | Motion doesn't seem to run | Old thread config names; user renamed to camera and fixed |
| #1397 | low | Enable color in still image | How to enable colour; bulk closed, no answer |
| #1383 | low | Installing on Raspbian Buster, package not found | Buster package names; users share working install substitutions |
| #1380 | low | Frame Change Threshold setting 0% | Threshold zero stops motion detection; reporter records own finding |
| #1376 | low | Kernel Oops after a few days of operation | Kernel Oops solved by lowering CPU frequency |
| #1367 | low | Test Service and Test Email buttons non-responsive | Buttons unresponsive in Edge; reporter's browser choice, own mistake |
| #1348 | low | Install problems with Raspian Buster | Buster install problems; package substitutions and workarounds discussed |
| #1337 | low | More settings? | Asks about more settings and plugins; answered, docs mention noted |
| #1288 | low | Video toot fast | Fast playback; PTS problem, updating Motion suggested and tried |
| #1284 | low | Raspberry Pi configuration has less than Ubuntu/Lubuntu | Missing options; reporter copied config files, settings appeared |
| #1185 | low | Save Videos To USB Drive From Remote Camera | Asks how to store remote camera videos; closed as stale |
| #1170 | low | problem configuring my camera | Tornado incompatibility; told to upgrade motionEye or downgrade Tornado |
| #1168 | low | Motioneye 0.39.3 fail to startup - Ubuntu server 16.04LTS | Startup failure solved by installing tornado 5.1.1 |
| #1161 | low | Threads problem | High CPU from Motion; setting explained it, no defect found |
| #1110 | low | Correct time in motionEye running in docker on an Ubuntu server | Docker time configuration how-to; closed by reporter, no comments |
| #1106 | low | Can't reach webinterface after enabling "Fast Network Camera" | motionEyeOS locked out; solved by deleting config files over SSH |
| #1100 | low | Shutdown not possible while pyton script is running | Posted in wrong repository; author moved it to motioneyeos (agent: invalid, changed in review) |
| #1078 | low | Opening picture/motion browser takes a while (20/30s) | Slow browser due to many pictures; reporter reduced retention |
| #1048 | low | Doc bug? Installation issue "No module named 'settings' | Python 3 used instead of Python 2; users' environment |
| #1023 | low | performance problems on large installation - Debian 9.5 / 27 Cams / 24 | CPU load from Motion on many streams; no motionEye defect |
| #1018 | low | Version `CURL_OPENSSL_3' not found | libcurl mismatch after OS upgrade; solved by package change |
| #1016 | low | motioneye not starting after upgrading ubuntu 16.04 to 18.04.1 | Not starting after Ubuntu upgrade; existing workaround linked |
| #942 | low | Authentication failed | Maintainer advises basic auth for RTSP; other schemes not implemented |
| #907 | low | Cannot pip install motioneye | Install fixed by using a different pip version |
| #851 | low | I can't install motioneye to Rasberry PI 3B+ ? | Missing zlib package; wiki dependencies updated as a result |
| #827 | low | Fatal Python error: GC object already tracked | Likely Python problem; reporter's upgrade via pip resolved it |
| #809 | low | Raspbian Install Issue | Startup error solved by installing with pip2; asks wiki note |
| #805 | low | Video downloads | Reporter concludes VLC dislikes the files; uses other players |
| #765 | low | Unable to connect IP Camera | Very old versions; upgrade advised, outcome not stated |
| #712 | low | old genius webcam not working | Solved by config addition found in a Motion issue |
| #695 | low | Motioneye is insecure by default (download last picture without user/p | Security concern discussed; maintainer explains signatures, no fix visible |
| #663 | low | NOIR and wifi fail after web update to MEyeOS 20170710 | motionEyeOS update broke old system; clean install solved it |
| #654 | low | MotionEye saves images and mp4 but can't retrieve them | motionEyeOS media listing; maintainer redirected reporter to that repo |
| #651 | low | As of latest update, port 8081 doesn't accept the username/password an | Auth failure sorted out by reporter; reporter apologized for confusion |
| #625 | low | WARNING: Connect error on fd 15: ECONNREFUSED | Maintainer: not valid motionEye issue, check Motion log; FPS expectations |
| #623 | low | No camera image | Worked after using normal OS image instead of minimal |
| #570 | low | cant play sound on motion detect | Sound on motion; commenters suggest path mistake, links related issue |
| #564 | low | Not able to add Vstarcam web-cam with rtsp, but rtsp works with VLC. | RTSP camera setup; commenter solved with correct port setting |
| #533 | low | Odroid XU4 Open Media Vault | Install on Odroid fixed after apt upgrade and reinstall |
| #520 | low | Improving performance | Motion behaviour question; redirected to Motion project |
| #518 | low | SSL certificate problem: self signed certificate | Self-signed certificate error; workaround validate_certs false option given |
| #498 | low | Shutter speed or iso setting (blurry picture in still images) | Asks how to set shutter speed or ISO; no answer |
| #471 | low | arch linux antergos installed ok but An error occurred. Refreshing is | Arch install; motion-git conflict with motion resolved reporter's error |
| #461 | low | Problem with Jessie/RaspiCam | Camera device problem; maintainer says not motionEye-related |
| #396 | low | Record error | Old Motion from Armbian lacked mp4; moved to Arch |
| #359 | low | Is there a chance to get Motioneye work without a constant network lin | motionEyeOS how-to question; author says posted here by mistake |
| #351 | low | surveillance user | Reporter found problem in own prefs.json |
| #336 | low | Error Unable to open video device with two different cam | motionEyeOS camera problem; reporter moves it to that repo |
| #295 | low | Feature request: change interval of snapshots | Requested setting already exists; maintainer shows where |
| #291 | low | Banana Pi CSI camera not selectable in GUI | Unsupported board hit 3s timeout; user patched locally |
| #274 | low | Web-UI -> Motion Notifications Settings Issue | Settings misplaced with old config; reconfiguring from scratch fixed it |
| #266 | low | monitor script | How to use monitor script; sample fixed in motionEyeOS |
| #246 | low | Any chance of adding motion boxes or areas? The software is awesome ot | Mask capability already exists; explained and added to wiki |
| #239 | low | Gmail refuse to accept mail from motioneye | Gmail refuses low-security apps; no motionEye defect found |
| #199 | low | using higher H264 streams and non standard resolution with MotionEye | Camera stream questions; thread drifted, maintainer lost track |
| #193 | low | Motioneye can't control motion detection | Maintainer suggests working schedule option; no confirmation |
| #145 | low | Re-authorizing Google Drive | Re-authorization solved by user removing uploadservices.json; no defect confirmed |
| #133 | low | Capture last motion detected snapshot image. | Request answered by existing lastsnap and snapshot URL |
| #79 | low | SVG images have wrong content-type | Missing system mime-types package; reporter says not motionEye issue |
| #67 | low | MotionEye camera view doesn't work when motion auth is enabled | Solved by upgrading and re-adding the camera |
| #62 | low | Failed to start, no useful error message | Start failure solved with working Motion binary; closed after help |
| #44 | low | Acces lost | Offline access problem solved by installing pytz |
| #33 | low | Still images are saved but not movies during motion detection | Solved support thread; exact cause not shown in comments |
| #13 | low | Message: An error occurred. Refreshing recommended. | Motion compiled without ffmpeg; install wiki updated |
| #4 | low | usb webcam no more working | Storage path setting fixed raspicam; webcam blamed on kernel |
| #1935 | high | ESP32-CAM | Correct stream URL given; reporter confirms it works |
| #1934 | high | 2 XBox 360 cameras connected to Pi Model B only one showing picture | Identical USB camera IDs limitation; reporter switched cameras |
| #1933 | high | Ubuntu 20 - Motioneye Web UI issue | Needed Python 2; reinstall on Ubuntu 18 solved it |
| #1932 | high | missing video playback | Reporter found mp4/h.264 format enables playback |
| #1927 | high | lastsnap.jpg not uploaded via (S)FTP | Reporter learned lastsnap.jpg is a symlink; nothing wrong |
| #1906 | high | mpeg4 network camera stream not working | Outdated drivers on reporter's Pi; reporter resolved it |
| #1893 | high | Video recording save pictures | Reporter fixed by disabling picture saving; settings matter |
| #1879 | high | What can i do to improve my setup? | Asks how to improve setup performance |
| #1878 | high | Ngrok Installation tutorial? | How-to about installing ngrok on motionEyeOS |
| #1875 | high | Any way to update OS from CLI | How-to about updating OS from CLI |
| #1872 | high | Can't add new Network camera motionEye 0.42 | Removing credentials from URL fixed it |
| #1871 | high | Motioneye in docker no networkshare possible | Mount shares on Docker host; answered and accepted |
| #1869 | high | Installation ubuntu 20 in Proxmox | Install help; gcc missing on user's system |
| #1860 | high | Viewing Video File Created by MotionEye | Viewing mp4 file; reporter used VLC instead |
| #1858 | high | Install On Raspbian failing at step 5 | Wrong pip used; instructions confirmed working |
| #1854 | high | Does frame change threshold need to change when I add a mask? | Threshold and mask behaviour answered from Motion docs |
| #1853 | high | ZeroCam support | Worked after selecting MMAL camera |
| #1851 | high | Ubuntu 20.04 LTS | Python 2 missing on Ubuntu 20.04; install workaround worked |
| #1837 | high | Port Forward and Port Triggering | Router port forwarding question; reporter answered himself |
| #1831 | high | Video not showing on frontend | Low container RAM and port conflict; user fixed |
| #1820 | high | File Storage problem | Reporter's low power supply caused storage problem |
| #1812 | high | Why is the recording size with passthrough 1/8 of that with overlay? | Asks why bitrate differs; explanatory discussion, no defect |
| #1811 | high | Motioneye & MotioneyeOs code | Asks what the code was written in |
| #1801 | high | How to fix this fake detection ? | False detections solved by tuning noise level settings |
| #1797 | high | Day & night vision question | Asks about day and night camera hardware |
| #1795 | high | How to access Motioneye remotely | Remote access how-to; wiki link answered it |
| #1791 | high | motion detection command | Reporter error; video was still being processed |
| #1789 | high | VLC Input | Asks whether VLC can stream into motionEye |
| #1783 | high | root directory.. where is? | Asks about storage path under Home Assistant addon |
| #1782 | high | Question: Using multiple NIC on MotionEye | Multiple NIC setup question; answered with routing explanation |
| #1781 | high | Motioneye on an old video server (videosafe) | Asks whether old video server capture works with motionEye |
| #1778 | high | change from moioneyeOS to motioneye | Asks how to add remote motionEyeOS camera |
| #1777 | high | Picture too small at 1920x1080 | Reduced field of view is Pi camera limitation |
| #1776 | high | motioneye installation requirement | Asks how to install libcurl and pycurl requirements |
| #1775 | high | How to "Add an init script, configure it to run at startup" | Install how-to; commands in the wiki step explained |
| #1772 | high | iFrame based on Streaming URL | Asks URL syntax for streaming in iframe |
| #1760 | high | Is it possible to "host" a txt file through the motionEye front end? | How-to about hosting a text file; reporter used another approach |
| #1759 | high | Compatibility with ONVIF events | Asks about ONVIF event triggering; reporter answered it himself |
| #1757 | high | Don't save to SD card | How to avoid local storage; answered with preserve settings |
| #1756 | high | Difference between simple MJPEG and Network camera? | Asks difference between simple MJPEG and network camera types |
| #1751 | high | Motion Detection video length question | How to set capture length; collaborator answered |
| #1750 | high | movie playback not working in browser | Reporter's ffmpeg install was broken; reinstalling fixed it |
| #1738 | high | rpi multicam with master hub | Multi-camera hub setup how-to; answered and worked |
| #1732 | high | Is it safe to upgrade to motion 4.3.1? | Asks if Motion upgrade is safe; reporter answered himself |
| #1728 | high | Motioneye cannot connect to remote Motioneye using the generated Strea | Wrong camera type chosen; commenter explains the correct setup |
| #1722 | high | Cam DID number | How to add app-only camera without credentials; support thread |
| #1721 | high | ONVIF cam | Asks where ONVIF is; answered with rtsp or mjpeg paths |
| #1720 | high | New Motion version | How to update Motion; answered with apt update |
| #1718 | high | [QUESTION] Pass though video stream to web client without re-encoding? | Labelled question about stream passthrough; answered by users |
| #1714 | high | Cameras found, but no image | Solved by installing Motion 4; hardware too weak |
| #1706 | high | Adding a camera creates problems | User had duplicate streaming ports; maintainer's hint fixed it |
| #1705 | high | Where does the raw files get saved in the System. | Asks where files live to modify interface; resolved by reporter |
| #1704 | high | FR: Possibility to turn cameras on and off | Requested buttons already exist; pointed to Action Buttons wiki |
| #1701 | high | Can I use MotionEyeOs for Commercial product | Licensing questions on commercial use; answered by maintainer |
| #1699 | high | Motioneye from Docker Hub - Missing "File Storage" Option missing | How to store on NAS share in docker; settings shared |
| #1697 | high | Action button Python path issue | Python module installed for wrong user; reinstall as root advised |
| #1691 | high | cannot add MJPEG camera (already added before) | Cause was reporter's full SD card |
| #1690 | high | run without installation as service | How to run without service; maintainer gave the command |
| #1687 | high | MotionEye: Unable to open video device on Raspbian 10 | Camera cable installed incorrectly; reporter fixed it |
| #1686 | high | Cannot reach web ui | Install used wrong pip version; reporter figured it out |
| #1681 | high | Is there a way to install and run motioneye on MacOS ? | Asks how to install on macOS; docker suggested |
| #1680 | high | alprd is consumming cpu | alprd came from unrelated jeedom plugin, not motionEye |
| #1679 | high | Execute ffmpeg command from Node-Red (running from container) | How to run ffmpeg from Node-Red container; no answer |
| #1678 | high | Docker is not building | Building outdated 0.37 source; told to update, CI works |
| #1667 | high | default user & password? | Asks default login; reporter answers admin with no password |
| #1664 | high | snapshot url, can i use it without authentication? | Asks about snapshot URL authentication; maintainer explains the signature |
| #1660 | high | inline help question marks | Missing inline help was browser cache; hard reload fixed it |
| #1655 | high | No picture in motioneye | Android app problem, wrong project; reporter redirected |
| #1654 | high | camera settings missing | Settings hidden because logged in as user, not admin |
| #1649 | high | Looking for guidance for storing videos on an SMB share | SMB setup guidance; address was unreachable from the Pi |
| #1645 | high | Cannot open video device or no video device available | Reporter had selected the wrong camera; own mistake |
| #1644 | high | Stretch => Buster : motioneye service KO | Solved by reinstalling pycurl following linked issue |
| #1639 | high | How do you solve the "Notification email failed: 5.7.9" error for Moti | Gmail needs an app password; answered |
| #1635 | high | mask. motion videos | Debug media files option explains the videos |
| #1634 | high | Command "python setup.py egg_info" failed with error code 1 in /tmp/pi | Reporter had not installed properly; own error |
| #1632 | high | camera video permission | Asks required permissions; answered by collaborator |
| #1631 | high | Adding Camera name to Filename | How to add camera name to filename; answered |
| #1628 | high | Clarification of mmal camera parameter passing | Parameter format question; reporter answered it himself |
| #1619 | high | Why streaming settings matter when streaming is off? | Asks why streaming settings affect capture; how it works |
| #1617 | high | Crop/Zoom MMAL | Crop/zoom solved with mmalcam_control_params roi option |
| #1615 | high | Web Interface not loading | Reporter's firewall blocked the ports; own setup |
| #1614 | high | Is motionEye available in OpenWrt? | Availability on OpenWrt; answered not available |
| #1612 | high | Docker installation exec format error | Wrong architecture Docker image; use the armhf tag |
| #1611 | high | Changing the mpeg4 profile? | Quality slider setting changed profile; reporter solved it |
| #1603 | high | How to setup Google Photos? | How to set up Google Photos upload |
| #1602 | high | How to calculate signature to generate a link to download movies? | How to compute movie link signature; how-to |
| #1601 | high | anything for esp32 / esp-eye ? | Asks about ESP32 support; answered as underpowered hardware |
| #1598 | high | leak option to add new camera | Missing camera option; maintainer says install Motion |
| #1596 | high | %f in web hook results in empty string | Maintainer explains %f unavailable on event start; use other hook |
| #1587 | high | Cant start motioneye on Alpine | Python 3 unsupported at the time; collaborator explains |
| #1586 | high | Motion Eye or Webcam Never Capture Human Movement | Tuning motion detection settings helped the reporter |
| #1584 | high | can't do much in setup_mode | setup_mode is a Motion option motionEye doesn't use |
| #1580 | high | [Motioneye][ubuntu 19.04] Update not updating [0.40 -> 0.42] | Upgraded without sudo; maintainer's tip fixed it |
| #1577 | high | Unable to set the amount of pics sent to cloud... | How to limit pictures uploaded; settings discussion |
| #1576 | high | Unable to configure Hiseeu IP camera | Camera configuration; working RTSP URL format supplied by commenter |
| #1568 | high | does motionexeos work on x86 or x64 hardware with debian installed | Asks x86 Debian support; answered with instructions |
| #1567 | high | Unable to access motionEye outside of network | Remote access port forwarding; reporter got it working |
| #1561 | high | restart event numbering (%v) at day change | Tip sought on resetting %v; maintainer suggests cron workaround |
| #1559 | high | I need better than 800x480 camera resolution | Pi Zero memory limits; settings advice given |
| #1558 | high | Using motioneye as server with more than 30 cameras | Hardware advice for many cameras; answered |
| #1554 | high | DS-2DE3304W-DE PTZ | Asks whether anyone got PTZ working; unanswered how-to |
| #1550 | high | ImportError: /usr/lib/x86_64-linux-gnu/libcurl.so.4: version `CURL_OPE | Post-upgrade libcurl mismatch; reporter solved by swapping libcurl package |
| #1549 | high | motion_control_localhost Setting Not Honored | Motion renamed option; webcontrol_localhost setting fixed it |
| #1547 | high | curl on webcontrol to add text only works without any spaces | URL encoding spaces solved the curl command |
| #1543 | high | How to disable /dev/video0? | Reporter found it was a configuration problem |
| #1542 | high | Installation process on raspbian | pip run without sudo; solved |
| #1537 | high | No static images in browser | Missing images; maintainer says install mime-types |
| #1534 | high | camera buffering no video | Old motionEyeOS with Chrome; update advised |
| #1521 | high | Unable to Connect to Web Interface | Default Python changed by user; force python2 in service |
| #1510 | high | docker not found | Needed explicit Docker image tag; reporter solved it |
| #1478 | high | cannot get motioneye work with nginx | Reporter's own nginx configuration issue, solved |
| #1474 | high | Motioneye on Fedora 31 (beta) | Told to use Python2; Python3 unsupported then |
| #1473 | high | Motioneye on raspbian not working | User used wrong port; works on 8765 |
| #1458 | high | Trying to run as normal user | pycurl SSL backend mismatch; solved by reinstalling with right environment |
| #1452 | high | Installation on Raspberry Pi 3B+ | Install trouble solved with right Docker image and clearing config |
| #1438 | high | Pictures are doubled (buster) | Debug media files option explained by collaborator |
| #1434 | high | motioneye wont start | Broken pycurl reinstalled on collaborator's advice; works |
| #1432 | high | No image from USB camera after installing motioneye | Fixed by manually installing newer Motion 4.2.2 |
| #1424 | high | Setting AWB for local Raspberry Pi camera | User error: apt Motion lacked mmal; not a motionEye issue |
| #1413 | high | No "advanced settings" button | Advanced settings removed by design; answered by maintainer |
| #1411 | high | Motion eye OS not recognizing my USB camera | Camera setup advice; user sent to research own camera |
| #1410 | high | Updating a docker installation with configuration preserved. | How to preserve Docker config; answered: use volumes |
| #1406 | high | Change Thumb Filename | Thumbnail naming not reproduced; matching filename structure resolved it |
| #1403 | high | Unable to send notification email | SMTP failure solved by using a different port |
| #1402 | high | Record a video by GPIO event | Asks if GPIO-triggered recording possible; pointed to existing issue |
| #1395 | high | Add username/password to already added rtsp camera stream | netcam_userpass via Extra Motion Options answered and worked |
| #1394 | high | Motioneye camera gets frozen | Freezing traced to underpowered Raspberry Pi 1 hardware |
| #1391 | high | Help getting a China 360 IP camera to work with motioneye | Unsupported cheap IP camera; reporter gave up |
| #1390 + dup | high | Unable to uprade MotionEye | MemoryError duplicate of #1230; --no-cache-dir solved it |
| #1389 | high | How do i use the command "sudo" on the Raspberry Pi Motion-Eye-OS? | motionEyeOS has no sudo; admin user is root |
| #1373 | high | Upload to Google Drive Failing - FIXED | Upload failures caused by full SD card |
| #1371 | high | motioneye fails to start after install | Install needs root; sudo pip solved it |
| #1370 | high | Setting "white balance" value for RPi camera via MotionEye | White balance set through Extra Motion Options; answered by reporter |
| #1366 | high | "Preferences - "Layout Columns" not visible and does not work on Safar | One column on mobile by design; reporter's misunderstanding |
| #1365 | high | Unable to access admin externally. | Wrong port used for external access; solved with help |
| #1346 | high | Cannot run application due to CURL_OPENSSL_3 not found | OS upgrade broke pycurl; release notes and reinstall solved |
| #1340 | high | Unabel to open video device | Wrong camera device chosen; mmal camera works |
| #1335 | high | Ignoring libssh2 on Raspbian | Maintainer: not a motionEye issue; system libssh packages fixed |
| #1329 | high | Insert a camera-stream from another motioneye | Fast Network Camera setting solved second motionEye stream |
| #1318 | high | Request: Is there a way to not show camera feeds until login? | Surveillance user password was unset; setting it solved |
| #1311 | high | Restore from Backup not working? | Missed config migration from release notes; solved |
| #1301 | high | Question (run in docker from hass.io): recommended way to store videos | How to store on USB in Docker; answered |
| #1292 | high | change date format | Date format; reporter found the text overlay setting |
| #1285 | high | MotionEye not showing video | Faulty camera hardware; replacement worked |
| #1262 | high | Errors in log and not detecting movement | Old Motion lacks option; member says update Motion |
| #1249 | high | How Does Login work in backend and in the client? | Third-party app login signature; own GET casing mistake fixed |
| #1238 | high | Unable to update | Reporter misunderstood 0.40 was only pre-release; user error |
| #1230 | high | Memory Error | pip MemoryError on Pi; --no-cache-dir solution helped users |
| #1228 | high | Ubuntu 16.04 install fails : bad directories | Install problem caused by missing sudo |
| #1225 | high | Rasbian motioneye can't update | pip upgrade killed by memory; solved with no-cache option |
| #1224 | high | Motion Notification - Run a Command | Run-a-command script solved by using mpg321 instead of GUI players |
| #1222 | high | Timestamp issue | Docker timezone; collaborator says bind mount correct zoneinfo file |
| #1209 | high | Not possible to update? | motionEyeOS update how-to; pointed to #1207, reporter admits mistake |
| #1205 | high | MotionEyeOS Login Modification | How to restrict access; answered with Nginx reverse proxy |
| #1199 | high | Total uninstallation? | Asks how to uninstall completely; fresh install suggested |
| #1196 | high | Can't find sata HDD | Drive partition not mounting; reformatting by user solved it |
| #1182 | high | Can we record remotely? | Asks about remote recording; hub setup explained |
| #1173 | high | Any available version for Debian 10 (buster) | Asks about Debian 10 support; maintainer answered |
| #1164 | high | Ubuntu Core? | Asks whether it runs on Ubuntu Core; no reply |
| #1160 | high | Docker container log WARNING: mjpg client connection for camera 3 on p | Log warning came from reporter's own streaming setting mistake |
| #1157 | high | Question: Pass-through Recording | How to enable pass-through; answered with extra motion options |
| #1153 | high | Missing features on Ubuntu? | Missing settings because cameras were added with wrong type |
| #1150 | high | lastsnap is overwritten by video thumbnail | Own script issue; webhook event setting was the cause |
| #1147 | high | Network cameras on debian | Camera setup; maintainer says select Remote motionEye Camera type |
| #1143 | high | Configuration confusion | Configuration question answered by maintainer |
| #1140 | high | Creating symbolic link? | Reporter says the issue was on Synology; no defect |
| #1139 | high | No camera on install Raspbian Stretch Pi 3B+ and Pi 3A+ | Missing video device; driver setup step on wiki was overlooked |
| #1134 | high | invalid credentials changing the URL | Custom base path modification; solved, reverse proxy suggested |
| #1132 | high | motioneye _ file storage problem | Upload failure traced to reporter's FTP server, not motionEye |
| #1130 | high | not a supported network camera - MJPEG | Wrong camera URL; maintainer says find real MJPEG URL |
| #1119 | high | Multiple instances of meyectl | Asks if multiple processes are normal; maintainer explains yes |
| #1109 | high | Solved - Broken videofiles | Broken videos caused by disconnected cameras in reporter's setup |
| #1108 | high | run motioneye with remote motion | Remote motion setup; maintainer says run motionEye on both |
| #1105 | high | RPi3 Recorded Video Skipping/Jumping | Video skips explained by motion gap and capture settings |
| #1101 | high | Question : does motioneye work with current motion versions? | Asks about Motion 4.2 support; collaborator says incompatible |
| #1099 | high | Can't connect to IP camera | Wrong Motion package installed; following guide solved it |
| #1091 | high | Motioneye Docker - Play recorded videos? | Old version; maintainer says upgrade motionEye and Motion |
| #1086 | high | More configuration around webhook payload | Requested webhook capability already exists; reporter found it |
| #1083 | high | lost pieces of viedo recording | Lost seconds explained by Capture After setting |
| #1082 | high | filter global movement | Existing Light Switch Detection solved camera shake triggers |
| #1073 | high | can't install motioneye | Docker volume path error; collaborator says user problem |
| #1065 | high | Misssing Setting | Hidden settings; maintainer says enable Advanced Settings |
| #1064 | high | Motioneye unable to connect to network camera | Camera connection; maintainer says find correct streaming URL |
| #1053 | high | Raspberry Pi motionEye (on Raspbian) high CPU usage | High CPU from limited hardware; reduce load or upgrade |
| #1049 | high | Can't enter text in a REQUIRED FIELD when trying to add new camera. | Invalid URL entered by user; maintainer explained |
| #1042 | high | Web refuses connection | Reporter forgot to use port 8765 |
| #1036 | high | Using ffmpeg command movie_end instead relayevent | Answered: use Extra Motion Options |
| #1034 | high | Multiple USB Cameras on high resolution | USB bandwidth hardware limit explained |
| #1031 | high | I created an API to get img online / offline | Help with own custom API code; solved via Stack Overflow |
| #1028 | high | Snapshot URL doesn't work on other clients | Signature depends on clock difference; maintainer explained |
| #1009 | high | Camera Select and Camera Remove Button defaulting to display none | Hidden buttons caused by add_remove_cameras setting being false |
| #1008 | high | motioneye autologin? | Autologin how-to; pointed to Useful URLs |
| #1004 | high | Applying settings through command line. | How-to about applying settings by command line; no reply |
| #1000 | high | How to https link cam? | HTTPS how-to; pointed to Nginx wiki page |
| #990 | high | Icons action buttons | Icon file location answered by maintainer |
| #983 | high | MotionEye Server/Hub without motion deamon? | Hub without Motion; maintainer explained existing camera type |
| #977 | high | Layout columns not working on RPI 7" Touchscreen? | Mobile layout behaviour explained; zoom out workaround given |
| #975 | high | 8081 port is not asking for authentication | Reporter found own configuration change caused it |
| #966 | high | Running MotionEye in Docker Container | Docker script how-to; answered with volume mapping |
| #953 | high | Settings panel missing 'Motion Detection' | Answer: enable Advanced Settings; reporter's oversight |
| #946 | high | camera stream sporadically lost | Reporter's client widget refresh caused it; changed client configuration |
| #939 | high | Cant start motion detection or edit streaming resolution | Reporter found the advanced option setting |
| #929 | high | Docker manifest | No latest tag; pointed to the wiki |
| #928 | high | URL with username and password for embedding | How-to on embedding with credentials in URL; reporter tries JS |
| #924 | high | Motion Notifications running when Motion Detection is disabled | Reporter's own changed port setting was the cause |
| #913 | high | SSL self signed certificate | motionEyeOS config path given; solved the reporter's problem |
| #909 | high | Adding a new Simple MJPEG Camera | Motion binary was not installed; user-side setup |
| #908 | high | Local Time not setting correctly | Reporter found the time zone setting |
| #898 | high | MotionEye fails to start after install - Raspbian Stretch | Ran under Python 3; fixed by reporter's shebang change |
| #894 | high | Motioneye settings doesn't show all settings | Reporter found Advanced Settings |
| #891 | high | Trouble downloading release for raspian | Reporter's network misconfiguration blocked the download |
| #886 | high | Failed to connect to localhost port 8081: Connection refused - Docker | Reporter used the wrong port; 8765 works |
| #881 | high | MotionEye and other apps on the same raspberry | Answered: use motionEye on Raspbian instead of motionEyeOS |
| #879 | high | Latest ffmpeg package update on arch seems to have removed a required | Reporter simply needed to update his AUR motion package |
| #878 | high | Docker container fails to start. | Reporter used an outdated repo and Dockerfile |
| #873 | high | No option to add "Network Camera"-- only "Simple MJPEG" and "Motioneye | Motion binary not installed; expected behaviour explained |
| #863 | high | Action Buttons on MotionEye under raspbian | Script permissions problem and typo on the user's side |
| #862 | high | Duplicate Cameras in Config : Feed not changing | Reporter forgot to change streaming port in manual config |
| #856 | high | How to change timezone via Docker installation on QNAP NAS? | How-to on timezone in Docker; pointed to wiki |
| #853 | high | upgrade error? | Wrong installation being restarted; clean reinstall advised |
| #848 | high | It doesnt work with the last update upgrade. | Solved by repeating the wiki install procedure |
| #838 | high | Different resolutions for video and still image | Resolved with extra Motion option for camera palette |
| #828 | high | Motioneye on stretch no run-command notification | Script ran as root, not pi; resolved via earlier issue |
| #810 | high | Motion Notification - Script does not execute. | Users helped reporter with script and logs; closed as solved |
| #798 | high | How do I set the time zone? | How-to on time zone; solved with dpkg-reconfigure tzdata |
| #795 | high | Higher CPU utilization with Raspbian than MotionEyeOS | Self-described question; reporter misread the top output |
| #793 | high | Need to edit motioneye.conf but I forget how to ssh in | Answered: motionEyeOS config lives in /data/etc |
| #780 | high | How to start the camera interface from Raspbian, where it is installed | How-to on local preview; maintainer explains limits |
| #769 | high | Set order of cameras? | Reporter found camera ID determines order |
| #758 | high | Optimal Hardware for Multiple High Quality Streams? | Hardware and GPU advice question; answered |
| #752 | high | event_image_snapshot: Could not create symbolic link | VirtualBox shared folder disables symlinks by default; user setup |
| #748 | high | Jessie to Stretch upgrade, error in directions step 7 | Reporter omitted sudo on pip install |
| #739 | high | movies not stored | Movies and motion detection simply needed enabling |
| #737 | high | Debian - Motioneye not running when SMB_share true | Missing cifs-utils package on reporter's system |
| #734 | high | Install problem Raspbian on pi3 | Install solved by update and dependencies per wiki |
| #731 | high | Issue installing Motioneye | Reporter accidentally installed with Python 3 |
| #729 | high | Help with installation of Motioneye on Raspbian | Install help; reporter found answer in an earlier issue |
| #720 | high | Insert my motioneye homepage in my html homepage | Embedding with password question; maintainer says not possible |
| #718 | high | Message: An error occurred. Refreshing recommended | Answered: clear browser cache and refresh |
| #713 | high | no static images showing up on centos7 | Missing mime.types file; installing mailcap solved it |
| #711 | high | no picture with mmal camera on pi | Old Motion version; upgrading fixed it |
| #707 | high | recorded movies aren't sorted propery | Sorting follows reporter's changed folder naming pattern |
| #701 | high | Enable debugging? | How to check debugging; answered |
| #689 | high | Limited menu options | Advanced Settings not enabled; reporter confirms |
| #681 | high | CentOS installation issues | Tornado import error; reinstalling tornado via pip suggested |
| #673 | high | Error on banana pi-m64 | Missing libraries for Motion install; not a motionEye issue |
| #667 | high | raspberry pi 3 camera not detected by motioneye | Solved by following another issue's install guidance |
| #665 | high | Cant add RTSP camera motioneye/Ubuntu16.04 | Fixed by using pre-built Motion binaries instead of distro package |
| #661 | high | Different between MotionEyeOS and MotionEYE? | Asks difference between motionEye and motionEyeOS; answered |
| #658 | high | email interval snapshots | How-to for interval emails; solved with own cron script |
| #656 | high | Picture file upload to server | Wrong FTP path format; correcting it solved upload |
| #655 | high | Install issue/query | Asks whether install is normal; answered yes |
| #652 | high | Help with FTP | FTP location configuration how-to; answered |
| #647 | high | Unable to view media | Too many media files; maintainer explains cleaning up |
| #643 | high | Cannot Install Motion on Raspian | Install dependency failure on Raspbian; instructions worked after apt-get update |
| #630 | high | Dead camera makes MotionEye unusable | Port conflict with Calibre on user's system; resolved by changing port |
| #618 | high | tornado.httpclient not found after upgrade to newest version | Stale symlink to old Python on user's system |
| #602 | high | when using action button - tricker a python script - I get error | Action button script missing shebang; user error |
| #599 | high | How do I stop Motioneye from saving the photos on the SD card | How-to about stopping local saves to SD card |
| #597 | high | How to flush config after restoring wrong config? | How to reset config; answered with a command |
| #594 | high | missing sliders in ui (centos 7) | Missing sliders solved by clearing browser cache |
| #591 | high | Scrolling Video / How to specify video format | Video norm how-to; solved with extra motion option |
| #582 | high | thread-2.conf over-ridden | User likely missed RTSP/UDP option; re-adding camera worked |
| #534 | high | banana pi | motionEyeOS boot failure from old image; newer file worked |
| #530 | high | Impossible to install motioneye on RPi2 | Install dependency errors solved by updating dependencies |
| #512 | high | Cannot write to motioneye.conf file | Reporter used the wrong command to edit file |
| #505 | high | motioneye | Motion not installed; installing it solved the problem |
| #489 | high | How to add bcm2835-v4l2 to /etc/modules | How to add module to /etc/modules; reporter found command |
| #485 | high | I'm trying a from-scratch install on Raspbian Jesse....." not debian f | Corrupt download; re-downloading the package solved it |
| #481 | high | Web interface missing settings? | Missing settings; maintainer says log in as admin |
| #458 | high | Red frame around feed? | Asks red frame meaning; reporter learned it means motion |
| #451 | high | Can't add RTSP camera due to URL formatting. | Reporter found correct RTSP URL with UDP; setup issue |
| #447 | high | Missing Icons on centos 7 | Missing mime.types; installing mailcap solved it |
| #438 | high | Nginx configuration : Request some help from community | Nginx reverse proxy help; reporter's config mistake solved |
| #435 | high | Play a sound on motion detection | Run-command sound help; maintainer says not motionEye issue |
| #432 | high | Wanting to record video and stills to my mac mini's usb connected driv | Network share setup help; reporter got it working |
| #430 | high | Error in base_path for reverse proxy | Reporter admits user error in reverse proxy config |
| #424 | high | Motioneyeos on Pi Zero with enc28j60 ethernet module | motionEyeOS boot config how-to; maintainer points to tweaks wiki |
| #418 | high | Text Overlay size and date format | Text overlay format how-to; answered with local config edit |
| #417 | high | new Camera ID field | Empty Camera ID fixed by clearing browser cache |
| #416 | high | OpenMV Board | Asks about OpenMV board support; answered unsupported hardware |
| #412 | high | How to create timelapse movies? | How to create timelapse; answered via media browser |
| #407 | high | How to handle brightness | Brightness handling how-to; solved with camera mode threshold tweak |
| #404 | high | Problem to install Motioneye on Ubuntu 16.04LTS | Pip install error on Ubuntu; solved with suggested commands |
| #397 | high | GPU motioneye? | Asks about GPU encoding; answered that Motion handles encoding |
| #395 | high | Temporary solution to trigger recording | Script workaround thread; carriage return in user's script fixed |
| #393 | high | Is there a way a change motion log level? | How to change Motion log level; answered by maintainer |
| #373 | high | Run a command | Run command needed python prefix; user setup solved |
| #371 | high | Question about config files | Explicit question about config files; no comments |
| #368 | high | Camera ID is empty | Empty Camera ID fixed by clearing browser cache |
| #367 | high | no local camera option | Camera was not connected correctly; reporter solved it |
| #356 | high | upgrade to new motion - need help ? | How to upgrade Motion; maintainer gives steps |
| #354 | high | Unable to see streaming when logged as normal user | Framerate dimmer setting was too low; solved |
| #352 | high | MotionEyeOS on Raspbian | Install problem solved by using pip2.7 |
| #349 | high | led control missing? | LED option exists only in motionEyeOS; not a bug |
| #346 | high | CSS | How-to about CSS files and remote cameras |
| #341 | high | failure updating on Raspbian Wheezy | Reporter admits user error during update |
| #339 | high | Saving stills but not videos | Upgrading to Motion 4 fixed missing movies |
| #337 | high | How To Store Motioneye still images or movies on PI 3 SD Card. | How to configure local file storage; answered |
| #333 | high | Missing NoIR camera [Pi Zero] | Missed loading camera module at startup |
| #332 | high | Motioneye Raspberrypi 3 WIFI Issue | Router changed Pi IP address; not a defect |
| #331 | high | motioneye service not starting on boot | USB mount order; solved with fstab suggestion |
| #325 | high | Motion notification won't run command. | Script lacked permissions and shebang; user side |
| #309 | high | pip install motioneye on raspbian error | Install error solved by pycurl package or upgrading pip |
| #305 | high | Reading log files | Newbie question about logs and media storage |
| #300 | high | Movie files not saved | Wrong Motion version for config; reverting fixed it |
| #298 | high | install on debian - no working gui | Reverse proxy base_path setup; maintainer explains |
| #297 | high | What is the "fps" overlay? | Asks what the fps overlay means |
| #292 | high | Camera not detected | Camera module not loaded; maintainer points to docs |
| #286 | high | Recorded videos "too fast" | Changing movie format setting fixed playback speed |
| #281 | high | Dahua H.264 camera | RTSP camera setup solved with manual config |
| #280 | high | Only basic menus after installation | Forgot to apply Advanced Settings; user mistake |
| #278 | high | Upload to gdrive does not work | Authorization key already redeemed; reused key on user side |
| #268 | high | MotionEye Gui - miss some settings | Reporter forgot advanced options setting |
| #265 | high | No thumbs file created automatically | Cause found by reporter; thumbs resolved, maintainer advises ffmpeg |
| #263 | high | relayevent.sh: Permission denied | Old pip version caused broken upgrade; user setup |
| #252 | high | Recorded and visualized video imperfections | Using TCP instead of UDP solved video imperfections |
| #247 | high | Adding remote motioneye camera | Storage was full; emptied and it worked |
| #244 | high | Network Share Option not offered | Network share option needs smb_shares setting |
| #238 | high | enable WiFi, motion not detected? | Motion detection was disabled in settings |
| #231 | high | Save movie files in mp4 format | MP4 output already possible with latest version |
| #226 | high | broken/missing icons on motioneye server | Missing mime.types file on CentOS; solved |
| #225 | high | motion recording not working on rpi3 | Recording settings were off; switching on fixed it |
| #220 | high | Image rasbian? | Install help; camera enabled and setup then worked |
| #219 | high | Motioneye can't connect to raspberry pi motion camera | Plain motion unsupported as remote; use motionEye on Pi |
| #216 | high | Email notification logs | Email failure was wrong username or password |
| #211 | high | resolution monitor and layout... | Layout on small display solved by browser zoom |
| #210 | high | Question: is it possible to trigger motioneye to turn camera on/off fr | Asks how to toggle camera from external scripts |
| #209 | high | there isn't network storage option | Set smb_shares to true; solved |
| #207 | high | not able to add pi camera module v2.1 noir | Camera not detected due to missing driver; user setup |
| #205 | high | Motioneye only showing Preferences | Needed to log in as admin for settings |
| #202 | high | Issue installing on Ubuntu 16.04 | Install problem solved by rerunning with sudo -i |
| #187 | high | Install MotionEye on Raspbian Wheezy for RTSP camera | RTSP install help on Wheezy; solved with library symlinks |
| #185 | high | Archlinux on Raspberry 3 : Cannot install MotionEye 0.31.4 | Reinstalling setuptools fixed install on Arch |
| #182 | high | trigger GPIO via 'Run Command' upon motion detection | How to trigger GPIO through Run Command; answered |
| #181 | high | RTC DS | RTC question; depends on OS, pointed to motionEyeOS |
| #180 | high | Is there a way to run motionEye on a windows machine | Asks about running on Windows; Linux only, answered |
| #176 | high | location for python scripts | Where to place notification script; answered |
| #173 | high | Failure to get wireless IP results in reboot loop | Fixing WLAN config on motionEyeOS; maintainer gives steps |
| #169 | high | Save last recorded image | How to save images on motion; maintainer answers |
| #167 | high | Issue with light | Light-change false alarms; pointed to Motion forums for tuning help |
| #166 | high | network camera help | Camera setup help; RTMP unsupported by Motion daemon |
| #163 | high | Error doing a pip upgrade | Pip upgrade failed; user lacked sudo permissions |
| #156 | high | Take a picture with a USB camera via command line | How-to on trees triggering motion; answered with mask feature |
| #155 | high | motioneye.log & motioneye.pid not created | Systemd no longer creates those log files; expected behaviour explained |
| #154 | high | is motioneye compatible with weaved | Compatibility question answered by another user |
| #152 | high | Google Drive location? | Asks Google Drive location syntax; how-to |
| #148 | high | System time | System time how-to; user's DNS and wifi config at fault |
| #143 | high | Webhook Lag | Webhook timing fixed by adjusting motion settings as advised |
| #139 | high | Multiple Cameras | Solved by updating all cameras to latest version |
| #128 | high | Local webcam not configurable or my config mess-up? | Webcam setup solved by replacing user's motion config |
| #126 | high | Thumbnails on recorded videos | Solved by installing missing libavresample2 package |
| #124 | high | IP-Camera as source | How-to on adding cameras; answered, works |
| #116 | high | Menu Options not appearing | Menus returned after disabling fast network camera setting |
| #108 | high | Raspbian - MotionEye | Imported config problem solved with new config directory |
| #107 | high | Motioneye Stream Freezes. | Stream freezes; logs show brownouts, replace power supply |
| #104 | high | Confused about continuous recording file logic | Motion file logic question; answered by maintainer |
| #103 | high | Empty motioneye.log | Empty log solved by adding -l option |
| #101 | high | motioneye wont start with systemd | Packages installed in user directory; reinstall as root solved |
| #100 | high | Empty snapshot | Empty snapshot solved by existing config setting |
| #98 | high | Extra Motion Options Field | Options are in thread config; user error acknowledged |
| #93 | high | Motioneye.service loaded failed failed | Install failure from missing MarkupSafe; manual install or reinstall solved |
| #88 | high | Question: ffmpeg precompiled | Asks about precompiled ffmpeg; solved using precompiled packages |
| #81 | high | Protocol rtsp not supported | RTSP needed a suitable Motion build; solved with SVN build |
| #74 | high | 'run a command' on motion detection | Script failed from carriage returns; user's own file |
| #70 | high | Motioneye upgrade on CentOS | Upgrade failed on missing curl-config package; reinstalled fine |
| #51 | high | Can't start after update! | Outdated config after update; copy new sample file |
| #47 | high | Mask Question | Mask question, answered in thread |
| #43 | high | Still images are saved but not movies during motion detection | Old version from outdated guide; reinstalling latest resolved |
| #38 | high | ./configure | Motion build steps problem; users supplied working command |
| #35 | high | Missing Icons Webinterface | Missing mime-types package on Arch; installing solved it |
| #34 | high | Can't install! | Install failed from permissions and old leftovers; user error |
| #27 | high | failed to read settings, unknown configuration option | Stray character in user's config file |
| #25 | high | How to install motioneye0.27 in raspberry pi2 | Install how-to; pointed to the wiki |
| #10 | high | Add local network file storage functionality | Request answered: already exists via smb_shares option |
| #6 | high | ERROR: decoder jpeg not available | Missing libjpeg-dev; reinstalling pillow solved it |
