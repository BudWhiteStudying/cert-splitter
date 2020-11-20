import sys
import os

VERBOSE_FLAG="-v"
VERBOSE = False

BEGIN_STRING='-----BEGIN CERTIFICATE-----'
END_STRING='-----END CERTIFICATE-----'
OUTPUT_DIR='./output/'
OUTPUT_FILE_NAME_PREFIX="google-cert-"
OUTPUT_FILE_NAME_EXTENSION=".pem"

def usage():
	print "\nUSAGE: python cert-splitter.py <input-file>\n"

def writeToFile(content):
	if not os.path.exists(os.path.dirname(OUTPUT_DIR)):
		os.makedirs(os.path.dirname(OUTPUT_DIR))
	outputFile = open(OUTPUT_DIR+OUTPUT_FILE_NAME_PREFIX+str(FILE_COUNT)+OUTPUT_FILE_NAME_EXTENSION, "w+")
	outputFile.write(content)
	outputFile.close()

if len(sys.argv)<2:
	sys.exit(usage())

if VERBOSE_FLAG in sys.argv:
	VERBOSE = True

if VERBOSE:
	print "input filename is "+sys.argv[1]
INPUT_FILE=sys.argv[1]

IS_WRITING = False
FILE_COUNT = 0
TEMP_FILE = ""
file = open(INPUT_FILE)
for line in file:
	if IS_WRITING:
		TEMP_FILE = TEMP_FILE + line
		if str(line).strip() == END_STRING:
			#print "Stop writing"
			writeToFile(TEMP_FILE)
			TEMP_FILE = ""
			IS_WRITING = False
			FILE_COUNT+=1
	else:
		if str(line).strip() == BEGIN_STRING:
			if VERBOSE:
				print "Writing file " + str(FILE_COUNT)
			IS_WRITING = True
			TEMP_FILE = TEMP_FILE + line
print "Split input file " + str(INPUT_FILE) + " into " + str(FILE_COUNT) + " .pem files"
file.close()