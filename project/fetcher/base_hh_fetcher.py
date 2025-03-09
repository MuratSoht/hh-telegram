from abc import ABC, abstractmethod
class BaseHhProccer(ABC):
    """
    Абстрактный класс, представляющий обработчик запроса к hh api, который выводит всю нужную информацию о вакансии
    """

    @abstractmethod
    def get_state(self):
        """
        Метод, который возвращает словарь, содержащий данные о вакансии. Словарь формируется засчет ниже перечисленных методов. 
        """
        pass

    @abstractmethod
    def get_id(self):
        """
        Метод, который возвращает id вакансии по hh api. 
        """
        pass
    
    @abstractmethod
    def get_title(self):
        """
        Метод, который возвращает название вакансии.
        """
        pass
    
    @abstractmethod
    def get_salary(self):
        """
        Метод, который возвращает зарплату вакансии
        """
        pass

    @abstractmethod
    def get_url(self):
        """
        Метод, который возвращает ссылку вакансии на сайте HeadHunter.
        """
        pass

    @abstractmethod
    def get_work_format(self):
        """
        Метод, который возвращает формат работы вакансии(в офисе, на месте работаделя, удаленно)
        """
        pass

    @abstractmethod
    def get_published_date(self):
        """
        Метод, который возвращает дату публикации вакансии.
        """
        pass

    @abstractmethod
    def get_city(self):
        """
        Метод, который возвращает город в котором необходимо работать.
        """
        pass

    @abstractmethod
    def get_experience(self):
        """
        Метод, который возвращает необходимый опыт для вакансии.
        """
        pass

    @abstractmethod
    def get_skills_keys(self):
        """
        Метод, который возвращает необходимые ключевые навыки для вакансии.
        """
        pass

    @abstractmethod
    def get_descriptions(self):
        """
        Метод, который возвращает описание вакансии.
        """
        pass

    @abstractmethod
    def get_archive(self):
        "Метод, который возвращает вакансия в архиве или нет (True или False)"