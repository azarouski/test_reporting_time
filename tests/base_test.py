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


def test_simple4(driver):
    logger.info("test4 finished")


def test_simple5(driver):
    logger.info("test5 finished")


def test_simple6(driver):
    logger.info("test6 finished")


def test_simple7(driver):
    logger.info("test7 finished")


def test_simple8(driver):
    logger.info("test8 finished")


def test_simple9(driver):
    logger.info("test9 finished")


def test_simple10(driver):
    logger.info("test10 finished")


def test_simple11(driver):
    logger.info("test11 finished")


def test_simple12(driver):
    logger.info("test12 finished")


def test_simple13(driver):
    logger.info("test13 finished")


def test_simple14(driver):
    logger.info("test14 finished")


def test_simple15(driver):
    logger.info("test15 finished")

