import sublime, sublime_plugin

class GoToPathCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		begin = view.sel()[0].begin()
		end = begin
		size = view.size()
		while True:
			c = view.substr(begin)
			if c == '\n':
				return
			if c=='"' or c == "'":
				break
			begin = begin - 1
			if begin<0:
				return

		begin = begin + 1
		while True:
			c = view.substr(end)
			if c == '\n':
				return
			if c=='"' or c== "'":
				break
			end = end + 1
			if end == size:
				return 

		folder_name = self.get_folder()
		root = view.settings().get("root")

		if root:
			root=root.replace("\\","/")
			if folder_name.find(root) != -1:
				root = folder_name
		else:
			root = folder_name

		pack_name = view.substr(sublime.Region(begin,end))
		pack_name = pack_name.replace(".","/")
		root= root  +"/"+ pack_name
		window = self.view.window()
		window.open_file(root)
	def get_folder(self):
		file_name = self.view.file_name()

		file_name = file_name.replace("\\","/")
		last_index = file_name.rfind("/")
		file_name = file_name[0:last_index]
		print(file_name)
		return file_name


