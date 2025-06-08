# TzDbLookup

Convert IANA time zone names (like `America/New_York`) to POSIX strings for use with SNTP and time zone configuration on embedded systems.

This library automatically syncs the database from the CSV file provided by https://github.com/nayarsystems/posix_tz_db/blob/master/zones.csv! Big thanks to nayarsystems for providing this!

## Usage

```cpp
#include <TzDbLookup.h>
const char* tz = TzDbLookup::getPosix("America/Los_Angeles");
