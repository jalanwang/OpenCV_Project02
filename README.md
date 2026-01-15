손글씨 숫자 인식을 이용한 보안 인증 시스템 구현

요약

컴퓨터 비전을 활용하여 사용자가 쓴 숫자 그림 4개를 인식하고 패스워드를 검증하는 시스템입니다.

입력 (Input): 웹캠으로 손글씨를 4회 캡처합니다. 사용자 편의를 위해 화면에 사각형 가이드라인을 제공합니다.

판단 (Logic): 사전에 학습된 파라미터(DNN)를 로드하여 입력된 이미지가 어떤 숫자인지 인식합니다.

결과 (Security): 성공 시 특정 메시지 생성. 키보드나 정전식 터치패드 없는 단말장치를 위한 인증 시스템을 설계하였다.

[link]Download (Linux)

Installation Instructions

Documentation

PLEASE FOLLOW AND TAG US!                 

Star History Chart

Version History
Detailed Release History

Version	Date	Comment
v3.6.0	Jan XX, 2026	Adds UI modes, adds support for Lebrew RoastSee NEXT and Acaia Pyxis Black (2025), 2DOF software PID implementation with interpolated gain scheduling, bumpless transfer and filtering, general stability and performance improvements.
❤️ Release Sponsor: artisan.plus ❤️
v3.4.0	Oct 31, 2025	Adds support for Kraffe, Berto, Nordic PLC, Prisma, additional Easyster and Proaster models, the latest Cogen and Toper roasters, and updates setups for Sweet Coffee Italia and Joper machines. Adds support for Tasi TA612C 4-channel and Shelly energy meters, as well as the ability to import Cropster profiles through drag-and-drop. Enables multi-day coffee fermentation experiments. Adds Czech and improved Chinese, Korean, and Spanish localizations. Updates the internal PID algorithm with advanced algorithmic and the app icon for the glass era (last version featuring legacy builds supporting macOS 10.13+, Window 8 and Windows 9).
❤️ Release Sponsor: artisan.plus ❤️
v3.2.0	Jun 23, 2025	Adds batch manager and support for the Acaia relay scales UMBRA and COSMO (last version supporting macOS 12, Ubuntu 22.04 and RedHat 8.4).
❤️ Release Sponsor: Acaia ❤️
v3.1.4	May 1, 2025	Fixes backward compatibility with some existing MODBUS configurations broken by v3.1.2
v3.1.2	Apr 30, 2025	Adds roast defects weight, event replay ramping, event dragging, Aillio Bullet R2 support, IMF machine control setups, extended support for Giesen machines, fixes Loring autoCHARGE/DROP, adds Carmomaq's Stratto Lab sample roaster, Phidget motor controllers, support for energy meters, ROEST CSV import, improved Cropster import, many small fixes and UI improvements
v3.1.0	Nov 22, 2024	Adds support for induction heated Gemma machines by Sweet Coffee Italia, the latest Santoker machines connecting via Bluetooth, Primo roasting machines, ColorTrack sensors, Stronghold profile import, and Phidget stepper controllers and more.
❤️ Release Sponsor: Algrano ❤️
v3.0.2	Aug 20, 2024	Bug fixes
v3.0.0	Aug 1, 2024	Adds roast scheduling support
❤️ Release Sponsor: artisan.plus ❤️
v2.10.4	Mar 21, 2024	Bug fixes
v2.10.2	Feb 29, 2024	Adds support for machines from Mill City Roasters, the IKAWA PRO X, the standard WinUSB driver for the Aillio R1 on Windows, the Digi-Sense 20250-07 IR, and the Extech 42570 IR.
v2.10.0	Nov 28, 2023	Adds support for Bühler Roastmaster, Joper, and Cogen roasting machines, the Phidget DAQ1000, DAQ1200, DAQ1300, DAQ1301, macOS AppleSilicon support, Raspbian Bookworm 64bit build, extra devices to Roast Comparator and many performance and stability improvements.
❤️ Release Sponsor: Paolo Scimone Coffee Consulting ❤️
v2.8.4	Jun 21, 2023	Adds official integration with Kaleido roasters as well as dark mode support on Windows and Linux (last version supporting macOS 11, but newer legacy builds still support macOS 10.13 and newer)
❤️ Release Sponsor: BC Roasters ❤️
v2.8.2	Dec 21, 2022	Adds support for Sivetz fluid bed roasting machines, Santoker Q Series and R Series roasters, the Yocto Watt module, the Phidget DAQ1500, and speeds up the Designer (last version supporting macOS 10.15, but legacy builds of v2.8 still supports macOS 10.13+)
v2.8.0	Oct 21, 2022	Adds support for new Besca models, Diedrich DR machines, Titanium Roasters, Eurotherm variants of San Franciscan machines, the Plugin Roast 2.0 module and CMS machines from Coffee Machines Sale, adds Roast Comparator phases widget and auto time axis modes
❤️ Release Sponsor: Coffee Machines Sales ❤️
v2.6.0	Mar 11, 2022	Adds support for a number of additional machines, the new Phidget HUB0001 and the Phidget VCP100x modules, the new generation Acaia Pearl-S/Pearl2021/Lunar2021 scales, adds a CHARGE timer, quadratic and RoR projections, an enhanced cursor coordinates widget, LCD cursor function, PDF reports, BBP support to Roast Comparator, some Roast Simulator enhancements, a slider mapping calculator, an artisan.plus custom blend editor, notifications, many keyboard shortcuts, Ukrainian localization, performance and stability improvements as well as macOS and Windows legacy builds
❤️ Release Sponsor: Showroom Coffee ❤️
v2.4.6	Jul 30, 2021	Adds energy and CO2 calculator, new setups for Probat UG and G Series machines with control functionality, the new FZ94 EVO machine by Coffee-Tech, as well as machines of Roastmax, Craftsmith and Carmomaq, updates Giesen setups to control additional actors on larger machines, adds support for the Yoctopuce modules Yocto-0-10V-Rx, Yocto-milliVolt-Rx and Yocto-Serial, extends Chinese and Spanish translations and adds translations for Vietnamese, Danish, Latvian, Slovak and Scottish (last version supporting Windows 8, but legacy build of v2.6.0 supports Windows 8)
❤️ Release Sponsor: Sweet Maria's ❤️
v2.4.4	Dec 14, 2020	Adds machine setups for the Nordic PLC and Fabrica Roasters, importers for Rubasse and Aillio RoastWorld, as well as PID Ramp/Soak pattern actions and templates (last version supporting Raspbian Stretch)
v2.4.2	Oct 2, 2020	Adds support for machines of over 40 brands including the Probat PIII series, IKAWA v3 CSV and RoastLog profile import, "Source Han Sans" and "WenQuanYi Zen Hei" font options providing complete Chinese, Korean and Japanese character sets, sliders Bernoulli mode, and WebSocket communication (last version supporting macOS 10.13 and 10.14; note that legacy builds of v2.6.0 and v2.8.0 again supports those systems)
v2.4.0	Jun 3, 2020	Adds Roast Comparator, Roast Simulator, and Profile Transposer, Cropster, IKAWA and Giesen Software profile import, flexible automatic file name generator, special event annotations, large PhasesLCDs, support for Twino/Ozstar roasting machines and the Giesen IR sensor, S7 and MODBUS protocol optimizations and extensions, support for additional Phidgets and Yoctopuce IO modules
v2.1.2	Dec 24, 2019	Bug fixes
v2.1.1	Nov 29, 2019	Bug fixes
v2.1.0	Nov 26, 2019	Adds profile analyzer, extended symbolic formulas, background images, forward looking alarms and alarms triggered by temperature differences, support for the Atilla GOLD plus 7" II, the Besca Bee sample roaster, additional Coffed machines (SR3/5/15/25/60), Coffeetool Rxx machines with control, and popular Phidget sets (incl. the one featured in On Idle Noise)
v2.0.0	Jun 4, 2019	New icon and new look! Adds support for the artisan.plus inventory management service, Coffee-Tech Engineering Silon ZR7, Has Garanti HGS and HSR series, Kaldi Fortis, and the forthcoming Behmor 1kg
v1.6.2	Mar 20, 2019	Enables communication with Phidgets under the Mac OS X 10.14 security framework
v1.6.1	Mar 10, 2019	Adds support for the Sedona Elite 2in1 roaster, the Probat Roaster Middleware, the Aillio R1 v2 firmware incl. the new IBTS IR sensor, the Phidgets REL1000, REL1100, REL1101, and DAQ1400, the Phidget RC Servo API (Phidget RCC 1000, Phidget 1061, and Phidget 1066), the Yocotopuce Meteo ambient sensor and the Yocotopuce IR module, adds Brazilian portuguese translations and updated French translations
v1.5.0	Oct 17, 2018	Adds ArtisanViewer mode, Phidgets IO VoltageRatio, Program 78 and Program 910 devices, and support for manual Besca roasting machines
v1.4.0	Oct 3, 2018	Adds time guide, additional PhasesLCD configurations, export/convert to Excel and import/export to Probat Pilot v1.4, channel tare, playback DROP event, always ON mode, support for ambient data and Phidget ambient sensors HUM1000 and PRE1000, PID P-on-Measurement/Input mode, improved curve smoothing, machine support for Atilla GOLD plus 7", Besca roasting machines, Coffee-Tech Engineering Ghibli and Diedrich Roasters
 v1.3.1	May 20, 2018	Adds support for Fuji PID PXF
 v1.3.0	Apr 15, 2018	Adds Siemens S7 support, MODBUS BCD decode, color themes, extraction yield calculator, support for machines of Aillio, BC Roasters, Bühler, Coffed, Coffee-Tech, Coffeetool, Giesen, IMF, K+M, Loring, Proaster, San Franciscan, Toper, US Roaster Corp
v1.2.0	Dec 21, 2017	Adds replay by temperature, support for Phidgets API v22, Phidgets USB devices USB 1002, 1014, 1017 and VINT devices HUB0000, TMP1100, TMP1101, TMP1200, OUT1000,OUT1001, OUT1002, OUT1100, VOLTCRAFT PL-125-T2, as well as the VOLTCRAFT PL-125-T4, improved RoR and dropout handling (last version supporting Mac OS X 10.12 and Linux glibc 2.17; first version requiring the Phidget v22 driver)
v1.1.0	Jun 10, 2017	Adds Recent Roast Properties, Aillio Bullet R1 profile import and support for Probat Probatone 2 (last version supporting OS X 10.9, Windows XP/7 and 32bit OS versions; last version supporting the Phidget v21 driver)
v1.0.0	Feb 24, 2017	Adds internal software PID, external MODBUS PID control, Apollo DT301, Extech 755, fast MODBUS RTU, AUC, RPi build, and additional translations
v0.9.9	Mar 14, 2016	Adds batch and ranking reports, batch conversions, follow-background for Fuji PIDs, additional keyboard short cuts, and designer improvements (last version supporting OS X 10.7 and 10.8)
v0.9.8	Oct 21, 2015	Adds US weight and volume units and extended symbolic expressions and plotter, ln()/x^2 approximations
v0.9.7	Jul 29, 2015	Bug fixes
v0.9.6	Jul 20, 2015	Bug fixes
v0.9.5	Jul 6, 2015	Adds Batch counter and app settings export/import (last Windows Celeron and Mac OS X 10.6 version)
v0.9.4	Jun, 6, 2015	Bug fixes
v0.9.3	May 15, 2015	Adds Phidget 1051, Hottop KN-8828B-2K+, and one extra background curve
v0.9.2	Jan 16, 2015	Bug fixes
v0.9.1	Jan, 3, 2015	Adds Acaia scale support and WebLCD QR code
v0.9.0	Nov 17, 2014	MODBUS ASCII/TCP/UDP, Yocto Thermocouple and PT100, Phidget 1045 IR, Phidget 1046 Wheatstone Bridge wiring, Phidgets async mode, Polish translations, LargeLCDs, WebLCDs, 2nd set of roast phases, volume calculator, moisture loss and organic loss, container tare, RoR delta span, phasesLCDs showing Rao's development ratio
v0.8.0	May 25, 2014	Phidget IO, Phidget remote, Arduino TC4 PID, Mastech MS6514
v0.7.5	Apr 6, 2014	Bug fixes
v0.7.4	Jan 13, 2014	Bug fixes
v0.7.3	Jan 12, 2014	Bug fixes
v0.7.2	Dec 19, 2013	Bug fixes
v0.7.1	Dec 2, 2013	Bug fixes
v0.7.0	Nov 30, 2013	Phidget 1046/1048, phases LCDs, xkcd style, extended alarms, Tonino support
v0.6.0	Jun 14, 2013	Monitoring-only mode, sliders, extended alarms, Modbus RTU, Amprobe TMD-56, spike filter, additional localizations
v0.5.6	Nov 8, 2012	Bug fixes  (last Mac OS X 10.4/10.5 version)
v0.5.2	Jul 23, 2011	Delta DTA PID support, automatic CHARGE/DROP
v0.5.0	Jun 10, 2011	HHM28, wheel graph, math plotter, multiple and virtual devices, symbolic expressions, custom buttons
v0.4.0	Apr 10, 2011	Localization, events replay, alarms, profile designer
v0.3.4	Feb 28, 2011	Arduino TC4, TE VA18B, delta filter
v0.3.3	Feb 13, 2011	Fuji PXR5/PXG5, manual device, keyboard shortcuts, Linux
v0.3.0	Jan 11, 2011	New profile file format
v0.2.0	 Dec 31, 2010	CENTER 300, 301, 302, 303, 304, 305, 306, VOLTCRAFT K202, K204 300K, 302KJ, EXTECH 421509
v0.1.0	 Dec 20, 2010	Initial release
License

OpenCV & Machine Learning 
 Login System

손글씨 숫자 인식을 이용한 보안 인증 시스템 구현

AI 로봇 소프트웨어 개발자 양성 훈련 과정

발표자: 김승혁


시연 영상

소스 코드

프로젝트 설명 자료 및 참조

YouTube 링크를 통해 실제 시스템 동작 모습을 확인하실 수 있습니다.

GitHub Repository에서 전체 소스 코드와 커밋 히스토리를 제공합니다.

OpenCV 4로 배우는 컴퓨터 비전과 머신 러닝 (황선규 저)
데이터 과학을 위한 파이썬 머신러닝
