# imgur upload 


## Installation

```
$ npm install -g imgur-upload-cli
```


## Usage

Uploading a single image:

```
$ imgur-upload path/to/image.jpg
```

-----

Uploading multiple images:

```
$ imgur-upload path/to/image-one.jpg path/to/image-two.jpg
```

Uploading multiple images with globbing:

```
$ imgur-upload path/to/*.jpg
```

Uploading latest image in a directory:

```
$ imgur-upload latest path/to/directory
```

Specifying default base directory:

```
$ imgur-upload basedir path/to/directory
$ imgur-upload latest
# will upload the latest image in path/to/directory
```

Deleting local copy of uploaded file (works for all upload commands above):

```
$ imgur-upload latest --delete
$ imgur-upload latest -d
```

View upload history:

```
$ imgur-upload history
```

Clear upload history:

```
$ imgur-upload clear
```



## Reference 

* [imgur-upload-cli](https://github.com/arnellebalane/imgur-upload-cli)