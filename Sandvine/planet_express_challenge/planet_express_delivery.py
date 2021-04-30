"""
Below goes a piece of quite questionable code which is supposed to implement the following scenario:
    1. An Employer is created with a number of Packages to deliver.
    2. The Employer hires a number of Workers.
    3. The Employer starts delivering the Packages having all Workers working simultaneously.
    4. Each Worker periodically asks the Employer for a Package to deliver.
    5. If any Package is available, the Worker delivers it and reports to the Employer.
    6. If there is no Packages left, the Worker finishes the work.
    7. The Employer periodically checks if all packages were delivered.
    8. If any Package is not yet delivered, the Employer waits a Worker to pick it up.
    9. If there is no Packages left to deliver, the Employer finishes the work.

The problem:
    The code seems to work, however, when the Employer prints statistics in the end of delivery,
    sometimes number of packages planned for delivery does not match number of packages reported
    as delivered by workers:
        [    INFO] employer: Total number of packages planned for delivery: 1000
        [    INFO] employer: Total number of packages delivered by workers: 1023

    It is noticed that the chance to face the problem is proportional to the total number of packages,
    so the code usually works fine for 10-100 packages, though almost always fails for 1000+.

Challenges:
    1. Improve the code to make it work for any number of packages.
    2. Improve the code to make it work faster.

Notes:
    * Feel free to make any changes to the code. The only what really matters is that all Packages get
      delivered by Workers in time, i.e. in the end each Package get mark_delivered() called by a Worker
      once and only once.
"""

import datetime
import logging
import threading
import time


class Package:
    """
    A package to deliver.
    """

    def __init__(self, name):
        self.name = name
        self.worker = None
        self.delivered = False

    def assign_worker(self, worker):
        self.worker = worker

    def mark_delivered(self):
        if self.delivered:
            raise Exception(f"Package {self.name} was already delivered")

        self.delivered = True


class Worker(threading.Thread):
    """
    Worker receives packages from employer and deliver them.
    """

    def __init__(self, name, employer):
        super().__init__()
        self.setName(name)
        self.employer = employer
        self.balance = 0
        self.packages_delivered = 0
        self.logger = get_logger(name.lower())

    def run(self):
        self.logger.info("Starting work")

        while True:
            package = self.employer.get_package_to_deliver()
            if not package:
                self.logger.info("No more packages to deliver")
                break

            self.deliver_package(package)
            self.employer.report_package_delivered(package)
            self.packages_delivered += 1

        self.logger.info("The work is fully done")

    def deliver_package(self, package):
        package.assign_worker(self)
        self.logger.info(f"Delivering package {package.name}")
        self.logger.info(f"Package {package.name} successfully delivered")


class Employer:
    """
    Employer hires workers and must deliver all packages.
    """#

    def __init__(self, packages_to_deliver):
        self.logger = get_logger("employer")
        self.packages = [Package(f"package_{n + 1}") for n in range(packages_to_deliver)]
        self.balance = len(self.packages)
        self.workers = []

    def hire(self, name):
        self.workers.append(Worker(name, self))
        self.logger.info(f"A new worker {name} was hired")

    the_lock = threading.Lock()

    def get_package_to_deliver(self):
        with self.the_lock:
            for package in self.packages:
                if not package.delivered:
                    return package

        return None

    def get_left_to_deliver(self):
        left = 0
        for package in self.packages:
            if not package.delivered:
                left += 1

        return left

    def report_package_delivered(self, package):
        self.balance -= 1
        package.worker.balance += 1
        try:
            package.mark_delivered()
        except Exception as e:
            self.logger.warning(f"A problem occurred while delivering the package: {e}")

        self.logger.info(f"Package {package.name} was delivered by {package.worker.name}")

    def deliver_all_packages(self):
        self.logger.info(f"Starting the work with {len(self.workers)} workers")
        start_time = datetime.datetime.now()

        for worker in self.workers:
            worker.start()

        while self.get_left_to_deliver() > 0:
            self.logger.info(f"Still {self.get_left_to_deliver()} packages to sent")
            time.sleep(1)

        self.logger.info("All packages delivered")

        for worker in self.workers:
            worker.join()

        work_duration = int((datetime.datetime.now() - start_time).total_seconds())
        self.logger.info(f"The work is fully done in {work_duration} seconds")
        self.logger.info(f"Employer balance: {self.balance}")
        total_deliveries_reported = 0
        for worker in self.workers:
            delivered = worker.packages_delivered
            total_deliveries_reported += delivered
            self.logger.info(f"Packages delivered by {worker.name}: {delivered}")

        self.logger.info(f"Total number of packages planned for delivery: {len(self.packages)} ")
        self.logger.info(f"Total number of packages delivered by workers: {total_deliveries_reported}")


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)8s] %(name)s: %(message)s"))
    return logger


def main():
    planet_express = Employer(10000)
    planet_express.hire("Philip")
    planet_express.hire("Leela")
    planet_express.hire("Bender")
    planet_express.hire("Amy")
    planet_express.hire("Hermes")
    planet_express.hire("Zoidberg")
    planet_express.deliver_all_packages()


if __name__ == "__main__":
    main()
