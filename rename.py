# Rename all email files in a folder to follow the naming convention:

# [dir-name] - email subject - MM.DD.YY date received

# Check that the new file name doesn't already exist. If it does:

# [dir-name] - email subject - MM.DD.YY (n)

import os

path = input('📂 Where are the files you want to rename? ')
protocolName = os.path.basename(path)
listing = os.listdir(path)
newFilenames = {}
dupeCount = 0
months = { 'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12' }

for eml in listing:
  if str.lower(eml[-3:]) == 'eml':
    f = open(path + '/' + eml)
    print('📥 Opening ' + eml + '...')

    for line in f:
      if line.startswith('Subject: '):
        subj = line[9:].rstrip()
        # TODO: Handle emails with no subject
        # TODO: Strip emoji from subject 😿

        print('📨 Getting subject line...')

      if line.startswith('Date: '):
        day = line[11:13]
        month = line[14:17]
        year = line[18:22]

        # TODO: Split string into list to get values instead of substrings

        print('📆 Formatting date...')

        for value in months:

          if value == month:
            month = months[value]

        formattedDate = month + '.' + day + '.' + year

    newFilename = protocolName + ' - ' + subj + ' - ' + formattedDate

    if newFilename not in newFilenames:
      newFilenames[newFilename] = 1
      newFilename = newFilename + '.eml'
    else:
      newFilenames[newFilename] += 1
      newFilename = newFilename + ' (' + str(newFilenames[newFilename]) + ').eml'

    print('📝 ' + eml + ' renamed to: ' + newFilename)

    os.rename(path + '/' + eml, path + '/' + newFilename)

print('🎉 Done! Your emails have been renamed.')
