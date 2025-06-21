import sublime, sublime_plugin
#I've had to sreencode many files at once. this helped
class SaveAsWinCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("save", {"encoding": "Western (Windows 1252)"})
        self.window.run_command("close")