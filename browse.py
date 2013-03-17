import sublime, sublime_plugin
from subprocess import Popen, PIPE

class BrowseCommand(sublime_plugin.WindowCommand):
    def run_browse(self, url, params):
        url = str(url)

        s = sublime.load_settings("Browse.sublime-settings")
        command = s.get("command");
        command.append(url)
        p = Popen(command, stdout=PIPE)
        text = "".join(line for line in p.stdout.readlines())

        v = self.window.new_file()
        v.set_name(url)
        v.set_scratch(True)
        edit = v.begin_edit()
        v.insert(edit, 0, text.decode('utf-8'))
        v.end_edit(edit)


class BrowseGoToCommand(BrowseCommand):
    def run(self):
        self.window.show_input_panel("URL", "", self.on_done, None, None)

    def on_done(self, url):
        self.run_browse(url, None)

class BrowseBookmarkCommand(BrowseCommand):
    def run(self):
        s = sublime.load_settings("Browse.sublime-settings")
        bookmarks = s.get("bookmark");
        self.window.show_quick_panel([x["name"] for x in bookmarks], self.on_done)

    def on_done(self, index):
        if index < 0:
            return
        s = sublime.load_settings("Browse.sublime-settings")

        url = s.get("bookmark")[index]["url"];
        self.run_browse(url, None)

