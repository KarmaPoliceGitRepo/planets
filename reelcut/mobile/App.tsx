/**
 * App.tsx — ReelCut mobile client (P6), iOS + Android via React Native.
 *
 * Scope (first increment): open a portable project doc, list kept clips, render
 * locally with ffmpeg-kit. Capture is a later increment. Nothing is uploaded —
 * the same local-first / no-egress guarantee as desktop (SR-1.7).
 */
import React, { useState } from 'react';
import { SafeAreaView, Text, FlatList, Button, View } from 'react-native';
import DocumentPicker from 'react-native-document-picker';
import RNFS from 'react-native-fs';
import { Project, keptSubs, render } from './src/render';

export default function App() {
  const [project, setProject] = useState<Project | null>(null);
  const [status, setStatus] = useState('Open a .reelcut project to begin');

  async function openProject() {
    const res = await DocumentPicker.pickSingle({ type: ['public.json', '*/*'] });
    const text = await RNFS.readFile(res.uri, 'utf8');
    setProject(JSON.parse(text) as Project);
    setStatus('Project loaded');
  }

  async function doRender() {
    if (!project) return;
    const out = `${RNFS.DocumentDirectoryPath}/episode.mp4`;
    setStatus('Rendering…');
    setStatus((await render(project, out)) ? `Done: ${out}` : 'Render failed');
  }

  const subs = project ? keptSubs(project) : [];
  return (
    <SafeAreaView style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 22, fontWeight: '600' }}>ReelCut</Text>
      <Text style={{ marginVertical: 8 }}>{status}</Text>
      <Button title="Open project" onPress={openProject} />
      <FlatList
        data={subs}
        keyExtractor={(s) => s.id}
        renderItem={({ item }) => (
          <View style={{ paddingVertical: 6 }}>
            <Text>{`#${item.order}  ${item.start.toFixed(1)}–${item.end.toFixed(1)}s`}</Text>
          </View>
        )}
      />
      {project && <Button title="Render" onPress={doRender} />}
    </SafeAreaView>
  );
}
