import dayjs = require("dayjs");
import * as vscode from "vscode";

let disposables: vscode.Disposable[] = [];
const titleRegex = /^#+\s/g;

export class CodelensProvider implements vscode.CodeLensProvider {
  constructor() {}

  public provideCodeLenses(
    document: vscode.TextDocument,
    token: vscode.CancellationToken
  ): vscode.CodeLens[] | Thenable<vscode.CodeLens[]> {
    const codeLenses = [];
    const regex = new RegExp(titleRegex);
    const text = document.getText();
    let matches;
    while ((matches = regex.exec(text)) !== null) {
      const line = document.lineAt(document.positionAt(matches.index).line);
      const indexOf = line.text.indexOf(matches[0]);
      const position = new vscode.Position(line.lineNumber, indexOf);
      const range = document.getWordRangeAtPosition(
        position,
        new RegExp(titleRegex)
      );
      if (range) {
        // [コマンドを呼び出すようにCodeLensを作成]
        codeLenses.push(
          new vscode.CodeLens(range, {
            title: "add date",
            tooltip: "add date",
            command: "markdown-date.addDate",
            arguments: [range],
          })
        );
        // [コマンドを呼び出すようにCodeLensを作成]
      }
    }
    return codeLenses;
  }

  public resolveCodeLens(
    codeLens: vscode.CodeLens,
    token: vscode.CancellationToken
  ) {
    return codeLens;
  }
}

export function activate(context: vscode.ExtensionContext) {
  console.log('Congratulations, your extension "markdown-date" is now active!');

  const codelensProvider = new CodelensProvider();
  let disposable = vscode.languages.registerCodeLensProvider(
    { language: "markdown" },
    codelensProvider
  );
  disposables.push(disposable);

  vscode.commands.registerCommand(
    "markdown-date.addDate",
    (range: vscode.Range) => {
      if (vscode.window.activeTextEditor) {
        const text = vscode.window.activeTextEditor.document.getText(range);
        const today = dayjs().format("YYYY-MM-DD");
        vscode.window.activeTextEditor.edit((editBuilder) => {
          editBuilder.replace(range, text + today + " ");
        });
      }
    }
  );
}

export function deactivate() {}
