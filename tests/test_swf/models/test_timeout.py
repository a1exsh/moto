from freezegun import freeze_time
from sure import expect

from moto.swf.models import Timeout, WorkflowExecution

from ..utils import make_workflow_execution

def test_timeout_creation():
    wfe = make_workflow_execution()

    # epoch 1420113600 == "2015-01-01 13:00:00"
    timeout = Timeout(wfe, 1420117200, "START_TO_CLOSE")

    with freeze_time("2015-01-01 12:00:00"):
        timeout.reached.should.be.falsy

    with freeze_time("2015-01-01 13:00:00"):
        timeout.reached.should.be.truthy
