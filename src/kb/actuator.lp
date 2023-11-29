sosakc_makesActuation(smartLight, illuminate).
sosakc_makesActuation(smartLight, not_illuminate).

sosakc_makesActuation(windowCover, open_cover).
sosakc_makesActuation(windowCover, close_cover).

sosakc_makesActuation(alarmSiren, warn_of_danger).
sosakc_hasFeatureOfInterest((alarmSiren, warn_of_danger), home).
