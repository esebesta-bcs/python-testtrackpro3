#!/usr/bin/env python

import logging
import datetime
import sys
import os
import testtrackpro

# Globals
scriptName = os.path.basename(sys.argv[0])
client = None # Leave this set to None
projectName = "Test" # Name of the project to login to
username = "administrator" # Username to login to the project with
password = "Password123" # Password to login to the project with
url = "http://127.0.0.1/ttsoapcgi.wsdl" # URL for the ttsoapcgi.exe to use
defectNumber = 1 # Number of the issue to edit. This is the defect number and not the record id.
customFieldLabel = "Test" # The name of a text custom field for defects
test_text = "PYTHON" # The text that will be appended to the summary, used in the above custom field, and the events notes field will be set to.
logLevel = logging.INFO # Change this value to "CRITICAL/ERROR/WARNING/INFO/DEBUG/NOTSET" as appropriate.

# Uses getProjectList() to retrieve a lists of projects from the server and then logs into the project
# that projectname is set to in the globals section. If successful it will return the client object to the calling function.
def login():
    max_retry_count = 3
    retry_count = 0
    ttp = None
    
    while retry_count < max_retry_count:
        if retry_count > 0:
            logging.error("Invalid TestTrack username/password combination, try again")

        ttp = testtrackpro.TTP(url, None, username, password)
        projects = ttp.getProjectList()
        project = None
        for p in projects:
            if p.database.name == projectName:
                project = p
        if project == None:
            logging.error("Invalid project name: %s", projectName)
            print("Invalid project name: ", projectName)
            sys.exit(-1)

        ttp.ProjectLogon(project)

        try:
            try:
                return ttp

            except KeyboardInterrupt:
                logging.info("... interrupted")

            except Exception as e:
                logging.error("User '%s' does not have access to TestTrack issues", username)
                return None
                
        except KeyboardInterrupt:
            logging.info("... interrupted")

        except Exception as e:
            logging.debug("Login failed, exception raised")

        retry_count = retry_count + 1

    if ttp == None:
        logging.error("Invalid TestTrack username/password combination")

    return ttp

def main():
    logging.basicConfig(filename=scriptName + '.log', level=logLevel, format=scriptName + ":%(levelname)s: %(message)s")

    client = login()
    if client == None:
        return -1
    else:
        logging.info("Successfully logged into the project")
        
    try:
        # With the way the testtrackpro python library was writen a saveDefect call is automatically performed when python finishes the following with block
        with client.editDefect(defectNumber, bDownloadAttachments=False) as defect:             
            # Append a dash and the contents of test_text to the summary of the defect
            defect.summary = defect.summary + " - " + test_text
            
            # Create a comment event
            event = client.create("CEvent")
            event.recordid = 0
            event.name = "Comment"
            user = client.getUserForCurrentSession()
            event.user = user.lastname + ", " + user.firstname
            event.date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            event.notes = test_text
            event.eventaddorder = 0
            #event.resultingstate = "Closed" # This is used if your event needs to have a resulting state set
            event.fieldlist = []
            # The following four lines show how to enter information for a custom field on the event
            #event.fieldlist.append(client.create("CDropdownField"))
            #event.fieldlist[0].recordid = 0
            #event.fieldlist[0].name = "Resolution"
            #event.fieldlist[0].value = "Code Change"
            # If the defect has no events create an empty eventlist for it
            if not hasattr(defect, "eventlist") :
                defect.eventlist = []
            # Add the event created above to the defect
            defect.eventlist.append(event)
            
            # If the defect has a custom field with the same name stored in customFieldLabel this will set the field to the value in
            # test_text or append test_text to existing text in the field.
            content = test_text
            for item in defect.customFieldList:
                if item.name == customFieldLabel:
                    if hasattr(item, "value"):
                        content = item.value + " " + content
                    setattr(item, "value", content)
                
        logging.info("Successfully edited defect #%s",defectNumber)
        return 0

    except Exception as e:
        logging.error("Failed editing defect #%s",defectNumber)
        logging.debug(e)
        print(e)
        return -1
        
#----------------------------------------------------------------------------
# python script entry point. Dispatches main()
if __name__ == "__main__":
    result = main()
    if client != None :
        client.DatabaseLogoff()
    exit(result)