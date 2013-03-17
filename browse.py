import sublime, sublime_plugin
from subprocess import Popen, PIPE

class BrowseCommand(sublime_plugin.WindowCommand):
    def run(self):
        s = sublime.load_settings("Browse.sublime-settings")
        command = s.get("command");
        command.append("http://www.apple.com/")
        p = Popen(command, stdout=PIPE)
        text = "".join(line for line in p.stdout.readlines())

        v = self.window.new_file()
        v.set_name("url or title")
        v.set_scratch(True)
        edit = v.begin_edit()
        v.insert(edit, 0, text.decode('utf-8'))
        v.end_edit(edit)
