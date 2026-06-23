const {getDefaultConfig, mergeConfig} = require('@react-native/metro-config');

/** Metro bundler config for ReelCut mobile. */
module.exports = mergeConfig(getDefaultConfig(__dirname), {});
