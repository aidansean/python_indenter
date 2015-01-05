import argparse, os.path, sys

# See https://docs.python.org/3.3/library/argparse.html

parser = argparse.ArgumentParser(description='indent some code')
parser.add_argument('-s', '--start' , metavar='start', type=int,
                   help='Start of indentation')
parser.add_argument('-e', '--end'   , metavar='end', type=int,
                   help='End of indentation')
parser.add_argument('-t', '--type'  , metavar='type', choices=['tab','space'], default='space',
                   help='Type of character to insert.  Valid options are: tab, space')
parser.add_argument('-n', '--nChars', metavar='nChars', type=int, nargs=1, default=4,
                   help='End of indentation')
parser.add_argument('-i', '--input' , metavar='file_in',
                   help='End of indentation')
parser.add_argument('-o', '--output', metavar='file_out',
                   help='End of indentation')
parser.add_argument('-c', '--comment', action='store_true',
                   help='Add comment at start and end of indentation')

args = parser.parse_args()

start = args.start if args.start else  0
end   = args.end   if args.end   else -1
comment = args.comment

#print args

filename_in  = args.input  if args.input  else ''
filename_out = args.output if args.output else ''

# Check to see if the user specifies an input file
if filename_in=='':
    print 'No input file specified!'
    sys.exit()
# If they do then check to see if file exists
if not os.path.isfile(filename_in):
    print 'Input file does not exist!'
    sys.exit()

# Now check to see if the user specifies an output file
if filename_out=='':
    print 'No output file specified!  Overwriting input file'
    filename_out = filename_in
elif os.path.isfile(filename_out):
    print 'Warning: will overwrite output file (%s)!'%filename_out

file_in = open(filename_in, 'r')

# Create the line prefix for the indented lines
char = ' ' if args.type == 'space' else '\t'
prefix = char*args.nChars

lines_in  = []
# Get lines in
for line in file_in:
    lines_in.append(line)

# Fix up the end if we need to
if end==-1:
    end = len(lines_in)-1

# Fix up the bounds in case the user asks for something outside the range of the file
start = max(start,1)
end   = min(end,len(lines_in))

if start > end:
    print 'end must be greater than start!'
    sys.exit()

lines_out = []
line_counter = 1
for line in lines_in:
    indent = False
    if line_counter < start:
        indent = False
    elif line_counter <= end:
        indent = True
    else:
        indent = False
    
    if line_counter == start and comment:
        lines_out.append('### Start of indentation\n')
    l = prefix + line if indent else line
    lines_out.append(l)
    if line_counter == end   and comment:
        lines_out.append('### End of indentation\n'  )
        
    line_counter += 1
file_in.close()

# Now we have indented everything
# Time to write it out
file_out = open(filename_out, 'w')
for l in lines_out:
    file_out.write(l)
file_out.close()

