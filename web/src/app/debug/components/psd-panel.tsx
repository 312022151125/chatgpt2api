"use client";

import { EditableFilePanel } from "./editable-file-panel";

const defaultPrompt = "Split the poster elements according to their original positions and compose an editable PSD. Preserve the background and each element's layer position, and export a zip of each layer asset.";

export function PsdPanel() {
  return <EditableFilePanel title="PSD Generation" kind="psd" endpoint="/v1/psd/generations" defaultPrompt={defaultPrompt} imageRequired />;
}
