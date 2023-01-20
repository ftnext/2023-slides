import * as vscode from "vscode";

export function activate(context: vscode.ExtensionContext) {
  console.log('Congratulations, your extension "markdown-date" is now active!');

  let disposable = vscode.commands.registerCommand(
    "markdown-date.helloWorld",
    () => {
      vscode.window.showInformationMessage("Hello World from Markdown Date!");
    }
  );

  context.subscriptions.push(disposable);
}

export function deactivate() {}
