import logging

from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

# Logger configuring
logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


def test_simple(driver):
    logger.info("test started")
    assert True
    logger.info("test finished")


def test_simple1(driver):
    logger.info("test1 finished")


def test_simple2():
    assert True
    logger.info("test2 finished")


def test_simple3():
    logger.info("test3 finished")
