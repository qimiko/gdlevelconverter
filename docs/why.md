# Why rewrite the old conversion tool?

The original conversion tool was based on code written almost 3 years ago. In this time, many developments have happened in the world of Geometry Dash knowledge that explain much of the code in the original tool. When it was originally written, a variety of values in the header, object, and even color string were unknown. Now, all of the values used by the converter are known, and more importantly, what they do in Geometry Dash is also known.

Much of later parts of the code was hacked onto the original code. For example, the illegal object report involved the use of a global variable, and group settings were just additional global variables on top of that. Groups themselves modified a global object conversion table. This all means that this script could only be run once, and would be impossible to integrate as part of a server as it'd need to reset state each time. This is no longer the case. The old "group" system was not easily extensible for this reason. The pre-1.9 header support was a rewrite of the 1.9 header conversion code, but with additional changes on top of that.

To support new developments like the creation of a standardized level format, the code needed to be significantly cleaned up. Otherwise, the code would become a half-duplicated mess...

## What's new?

* GDShare support
* Detailed object conversion groups
* Hopefully simplified usage