/**
 * render.ts — mobile render recipe (P6).
 *
 * The mobile client reads the SAME portable project document (SR-2.2) the
 * desktop app writes, and re-expresses the render as an ffmpeg-kit command. This
 * mirrors app/pipeline/render.py (extract kept clips, join with transitions),
 * keeping one model across all platforms.
 */
import { FFmpegKit, ReturnCode } from 'ffmpeg-kit-react-native';

export interface SubSection { id: string; start: number; end: number; order: number; keep: boolean; }
export interface Segment { keep?: boolean; subsections: SubSection[]; }
export interface Project { source: string; segments: Segment[]; }

/** Kept sub-sections in output order. */
export function keptSubs(project: Project): SubSection[] {
  const subs: SubSection[] = [];
  for (const seg of project.segments) {
    if (seg.keep === false) continue;
    for (const s of seg.subsections) if (s.keep) subs.push(s);
  }
  return subs.sort((a, b) => a.order - b.order);
}

/** Build the FFmpeg filtergraph: trim each kept clip, then concat. */
export function buildArgs(project: Project, outPath: string): string {
  const subs = keptSubs(project);
  const parts: string[] = [];
  subs.forEach((s, i) => {
    parts.push(`[0:v]trim=${s.start}:${s.end},setpts=PTS-STARTPTS[v${i}]`);
    parts.push(`[0:a]atrim=${s.start}:${s.end},asetpts=PTS-STARTPTS[a${i}]`);
  });
  const labels = subs.map((_, i) => `[v${i}][a${i}]`).join('');
  const fc = `${parts.join(';')};${labels}concat=n=${subs.length}:v=1:a=1[v][a]`;
  return `-y -i "${project.source}" -filter_complex "${fc}" -map "[v]" -map "[a]" ` +
         `-c:v libx264 -preset veryfast -crf 20 -c:a aac -b:a 192k "${outPath}"`;
}

export async function render(project: Project, outPath: string): Promise<boolean> {
  const session = await FFmpegKit.execute(buildArgs(project, outPath));
  return ReturnCode.isSuccess(await session.getReturnCode());
}
