# TzDbLookup

Convert IANA time zone names (like `America/New_York`) to POSIX strings for use with SNTP and time zone configuration on embedded systems.

## Usage

```cpp
#include <TzDbLookup.h>
const char* tz = TzDbLookup::getPosix("America/Los_Angeles");
