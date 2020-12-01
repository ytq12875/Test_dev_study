from mtf.core.context import Context
from mtf.core.logger import log
from mtf.core.testcasestore import TestCaseStore


def pytest_addoption(parser):
    parser.addoption(
        "--testcase",
        action="append",
        default=[],
        help='testcase yaml file or directory'
    )

    parser.addoption(
        "--include",
        action="append",
        default=[],
        help="testcase list",
    )


def pytest_configure(config):
    global option
    option = config.option
    log.debug(config)


def pytest_generate_tests(metafunc):
    testcase_dir = metafunc.config.getoption("testcase")
    testcase_include = metafunc.config.getoption("include")

    if len(metafunc.config.getoption('testcase')) > 0:
        context = Context()
        context.store = TestCaseStore()
        context.store.load(testcase_dir)
        log.debug(f'store={context.store}')
        TestCaseDemo.context = context
        #
        # if "store" in metafunc.fixturenames:
        #     metafunc
        #     metafunc.parametrize(
        #         "store",
        #         store.testcases.values(),
        #         ids=store.testcases.keys(),
        #         scope='module'
        #     )

        if "testcase" in metafunc.fixturenames:
            metafunc.parametrize(
                "testcase",
                context.store.testcases.values(),
                ids=context.store.testcases.keys(),
                scope='module'
            )
