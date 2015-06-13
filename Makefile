JAVA ?= java
SMC ?= java -jar tools/smc/smc_6_5_0/bin/Smc.jar
SOURCES += 

.PHONY: all
.SUFFIXES: .sm .java

all: $(SOURCES)

.sm.java:
	$(SMC) -java $(<)
