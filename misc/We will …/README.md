## We will …
The main idea to find the flag is to crack the zip's password using JohnTheRipper.
#### Step-1:
After I downloaded `beautiful.zip`, I tried using `zip2john` and cracked it with common list buster `rockyou.txt`

#### Step-2:
I got the password as: `cookiesrgood2`

#### Step-3:
So, I just extracted all the contents and got a directory named `beautiful` which had a image `something.jpg` in it.

<img src="something.jpg">

#### Step-4:
I used basic `strings`, `binwalk`, but no much use. So I used `Exiftool`

After input of command `exiftool something.jpg`, I got this output:

```bash
ExifTool Version Number         : 11.88
File Name                       : something.jpg
Directory                       : .
File Size                       : 631 kB
File Modification Date/Time     : 2020:08:20 19:20:28+05:30
File Access Date/Time           : 2020:08:25 18:54:21+05:30
File Inode Change Date/Time     : 2020:08:25 18:54:21+05:30
File Permissions                : rwxr-xr-x
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 96
Y Resolution                    : 96
Exif Byte Order                 : Big-endian (Motorola, MM)
Padding                         : (Binary data 2060 bytes, use -b option to extract)
Comment                         : CREATOR: gd-jpeg v1.0 (using IJG JPEG v62), quality = 100.
Warning                         : [minor] Fixed incorrect URI for xmlns:MicrosoftPhoto
About                           : uuid:faf5bdd5-ba3d-11da-ad31-d33d75182f1b
Lens Manufacturer               : flag{c00k13s_707@lly_ROCK}
Image Width                     : 1280
Image Height                    : 852
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1280x852
Megapixels                      : 1.1
```

Got the flag here.

#### Step-5:
Finally, the flag becomes:
`flag{c00k13s_707@lly_ROCK}`