from abc import ABC, abstractmethod


class AIProvider(ABC):
    """
    Strategy Pattern.

    AIProvider е абстрактна стратегия за комуникация
    с езиков модел.

    Различни AI доставчици могат да реализират
    този интерфейс по различен начин.
    """

    @abstractmethod
    def generate(self, prompt):
        """
        Генерира отговор на подаден prompt.
        """
        pass