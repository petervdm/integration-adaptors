import json
from fhirclient.models.operationdefinition import OperationDefinition
import adaptor.outgoing.interchange_adaptor as adaptor

with open("./mailbox/GP/TES5/outbox/patient-register-birth.json", "r") as patient_register:
    patient_register_json = json.load(patient_register)

op_def = OperationDefinition(patient_register_json)

(sender, recipient, interchange_seq_no, edifact_interchange) = adaptor.create_interchange(fhir_operation=op_def)

edifact_file = open(f"./mailbox/NHAIS/{recipient}/inbox/{sender}-{interchange_seq_no}.txt", "w")

pretty_edifact_interchange = "'\n".join(edifact_interchange.split("'"))

edifact_file.write(pretty_edifact_interchange)
edifact_file.close()
