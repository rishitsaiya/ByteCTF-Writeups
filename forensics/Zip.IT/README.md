## Zip.IT

The main idea to find the flag is to just keep on unzipping.

#### Step-1:
After downloading, `bytectf.zip`, we get a file `.a` extension added. So if we check the file format, it's a zip actually. Next if we try to change the extension to `.zip`, we get the recursion of files to `.a.b`, that way.

#### Step-2:
The main idea remains to first recursively extract all the zips and then reverse in the same order. We have to do this nearly 50 times.

#### Step-3:
Finally, the flag becomes:
`flag{K0mpr3SSi0N_n07_3nCryP7i0n}`