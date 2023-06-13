import logging

from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

# Logger configuring
logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


def test_simple():
    logger.info("test started")
    assert True
    logger.info("test finished")


def test_simple1():
    logger.info("test1 finished")


def test_simple2():
    assert True
    logger.info("test2 finished")


def test_simple3():
    logger.info("test3 finished")


def test_simple4():
    logger.info("test4 finished")


def test_simple5():
    logger.info("test5 finished")


def test_simple6():
    logger.info("test6 finished")


def test_simple7():
    logger.info("test7 finished")


def test_simple8():
    logger.info("test8 finished")


def test_simple9():
    logger.info("test9 finished")


def test_simple10():
    logger.info("test10 finished")


def test_simple11():
    logger.info("test11 finished")


def test_simple12():
    logger.info("test12 finished")


def test_simple13():
    logger.info("test13 finished")


def test_simple14():
    logger.info("test14 finished")


def test_simple15():
    logger.info("test15 finished")
