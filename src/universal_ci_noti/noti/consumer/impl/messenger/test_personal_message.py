from unittest.mock import AsyncMock, MagicMock

import pytest
from universal_ci_noti.messenger import Messanger
from universal_ci_noti.messenger.formatter import PlainFormatter
from universal_ci_noti.noti.types import Build, BuildStatus, JobResult, SCMInfo

from .personal_message import PersonalMessageConsumer

pytestmark = [pytest.mark.asyncio]


@pytest.mark.parametrize(
    "job_result,msg",
    [
        (
            JobResult(
                url="http://localhost/ci/repo_name_build",
                build=Build(
                    status=BuildStatus.SUCCESS,
                    number="1.21",
                    scm=SCMInfo(
                        url="http://github.com/repo_name.git",
                        branch="master",
                        commit="1234589",
                        name="repo_name",
                        committer="alex",
                    ),
                ),
            ),
            """🖥 Building repo_name(http://github.com/repo_name.git): SUCCESS
Branch: master
Committer: [alex]
Build page(http://localhost/ci/repo_name_build)""",
        ),
    ],
)
async def test_job_result_message(job_result, msg):
    messenger = Messanger()
    messenger.formatter = MagicMock(return_value=PlainFormatter())
    messenger.send_msg_to_user = AsyncMock()

    consumer = PersonalMessageConsumer(messenger)

    await consumer.on_job_finished(job_result)

    user_id, result = messenger.send_msg_to_user.call_args_list[0][0]
    assert user_id == job_result.build.scm.committer
    assert result == msg
