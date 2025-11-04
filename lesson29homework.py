#1
"""
Գրել MyShows class, որը․
   - __init__ ում կստանա
     -- սերիալի անունը (պետք է լինի տեքստ),
     -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ),
     -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
     -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
     -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
     -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
   - բոլոր ատրիբուտները կլինեն private,
   - կունենա getter բոլոր ատրիբուտների համար,
   - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
   - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
   - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
   - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։
"""


class MyShows:
    def __init__(self, name, platform, date, cast, episode=1, review=None):
        self._is_valid_name(name)
        self._is_valid_platform(platform)
        self._is_valid_date(date)
        self._is_valid_cast(cast)
        self._is_valid_episode(episode)
        self._is_valid_review(review)
        self.__name = name
        self.__platform = platform
        self.__date = date
        self.__episode = episode
        self.__review = review
        self.__cast = cast

    @staticmethod
    def _is_valid_name(name):
        if not isinstance(name, str):
            raise TypeError("name must be a string ")

    @staticmethod
    def _is_valid_platform(platform):
        if not isinstance(platform, str):
            raise TypeError("platform must be a string ")

    @staticmethod
    def _is_valid_date(date):
        if not isinstance(date, int):
            raise TypeError("date must be an int ")

    @staticmethod
    def _is_valid_cast(cast):
        if not isinstance(cast, list):
            raise TypeError("cast must be a list ")

    @staticmethod
    def _is_valid_episode(episode):
        if not isinstance(episode, int):
            raise TypeError("episode must be an int ")

    @staticmethod
    def _is_valid_review(review):
        if not (isinstance(review, int) and 1 <= review <= 10):
            raise TypeError("invalid review")

    @property
    def name(self):
        return f"name is {self.__name}"

    @property
    def platform(self):
        return f"platform is {self.__platform}"

    @property
    def date(self):
        return f"date is {self.__date}"

    @property
    def cast(self):
        return f"cast is {self.__cast}"

    @property
    def episode(self):
        return f"episode is {self.__episode}"

    @episode.setter
    def episode(self, value):
        self._is_valid_episode(value)
        self.__episode = value

    @property
    def review(self):
        return f"review is {self.__review}"

    @review.setter
    def review(self, new_review):
        self._is_valid_review(new_review)
        self.__review = new_review

    @review.deleter
    def review(self):
        del self.__review
        # print("change the review ")
        # self.__review=new_review

    def change_cast(self, ):
        print(f"cast: {self.__cast}")
        n = int(input("1-for appending, 0-for removing "))
        if n == 1:
            self.__cast.append(input("Enter a new name "))
            print(f"new cast: {self.__cast}")
        elif n == 0:
            t = input("Who you want to remove from a cast ").strip()
            if t in self.__cast:
                self.__cast.remove(t)
                print(f"new cast: {self.__cast}")

            else:
                print(f"{t} is not in a list ")
                print(f"new cast: {self.__cast}")

    def __repr__(self):
        return (f"{self.__name} ({self.__platform}, {self.__date})\n"
            f"Cast: {self.__cast}\n"
            f"Episode: {self.__episode}, Review: {self.__review}")

s = MyShows("The summer i turned pretty", "Netflix", 2022, ["Lola Tung", "Christopher Briney", "Gavin Casalegno"], 38,
            10)
print(s)
print(s.review)
s.review = 9
print(s.cast)
print(s.review)
print(s.episode)
s.episode = 30
print(s.episode)
s.change_cast()
s.change_cast()




