"use client";

import { EditableFilePanel } from "./editable-file-panel";

const defaultPrompt = "Create an 8-page business-tech style deck for the Q2 2026 e-commerce operations review, presented to company management. Highlight sales growth, user growth, ad performance, and 618 campaign results using line charts, bar charts, donut charts, and funnel charts.";

export function PptPanel() {
  return <EditableFilePanel title="PPT Generation" kind="ppt" endpoint="/v1/ppt/generations" defaultPrompt={defaultPrompt} />;
}
