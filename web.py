import webbrowser

def main():
	website = input("website: ")
	webbrowser.open(website)
	return main()

if __name__ == '__main__':
	main()
