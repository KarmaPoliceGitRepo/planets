/**
 * index.js — React Native entry point. Registers the ReelCut root component.
 */
import {AppRegistry} from 'react-native';
import App from './App';
import {name as appName} from './app.json';

AppRegistry.registerComponent(appName, () => App);
