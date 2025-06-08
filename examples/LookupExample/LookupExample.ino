#include <TzDbLookup.h>

void setup() {
  Serial.begin(115200);
  const char* iana = "America/New_York";
  const char* posix = TzDbLookup::getPosix(iana);

  if (posix) {
    Serial.printf("POSIX string for %s: %s\n", iana, posix);
  } else {
    Serial.println("Time zone not found.");
  }
}

void loop() {}
