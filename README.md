# text-editor-for-encrypted-files
This is a text editor to save and edit encrypted files of the extension .ankiecrypt  
this is fairly easy to use just like any other normal text editor.   
run - texteditor.py and not ankith.py  

## installation steps:
```bash
git clone "https://github.com/AnkithAbhayan/text-editor-for-encrypted-files" "ankith's text editor"
cd "ankith's text editor"
python -m pip install -r requirements.txt
cd "ankith's text editor\version - 1.3"
python texteditor.py
```  
another method would be to click the "download zip" button at the top (ie if you live in the 1960's)  
## how to run  
ez  
```bash
cd "ankith's text editor/version - 1.3/"
python texteditor.py
```  

## latest features
- latest version - v1.3(still working on it!).    
- title of the editor window will contain the file-size.
- added an 'exit' button in the file menu of the menubar to stop runnng.
- previously opened files can be accessed through the menubar as well.
- sys.argv arguments can be passed for opening in safe mode (no encryption and decryption on opening and closing). this allows you to open any type of file without changing the contents.
- "anonfalse" argument is equivalent to safe mode and "anontrue" argument is the basic mode (for opening .ankiecrypt files).

## TODO:
- make setup.py for adding files to path.
- make "open recent" button in the menubar work lol.
