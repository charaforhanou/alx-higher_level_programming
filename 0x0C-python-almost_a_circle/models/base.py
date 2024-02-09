se Module
"""
import json
import random
import turtle
import csv
from io import StringIO


class Base:
    """
    A Class that has a private attribute and constructor;
    __nb_objects and the __init__ function
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the class
        Args;
            id
        """
        if (id is None):
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list dictionaries
        Args:
            list_dictionaries is a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            io = StringIO()
            json.dump(list_dictionaries, io)
            return (io.getvalue())

    @classmethod
    def save_to_file(cls, list_objs):
        """It writes the JSON string rep of list_objs to a file
        Args:
            list_objs is a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        lst = []
        if list_objs is not None:
            for i in list_objs:
                lst.append(cls.to_dictionary(i))
        with open(filename, "w") as file:
            file.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        Args:
            json_string is a string representation of a list of dict
        """
        lst = []
        if json_string is None or len(json_string) == 0:
            return lst
        else:
            io = StringIO(json_string)
            return (json.load(io))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attribute already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        lst = []
        try:
            with open(filename, "r") as f:
                lst = cls.from_json_string(f.read())
            for k, v in enumerate(lst):
                lst[k] = cls.create(**lst[k])
        except Exception as e:
            pass
        return lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as f:
            csvwriter = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csvwriter.writerow([obj.id, obj.width, obj.height, obj.x,
                                        obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csvwriter.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSv"""
        filename = cls.__name__ + ".csv"
        lst = []
        try:
            with open(filename, 'r') as fcsv:
                csvreader = csv.reader(fcsv)
                for attr in csvreader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                                "id": int(attr[0]),
                                "width": int(attr[1]),
                                "height": int(attr[2]),
                                "x": int(attr[3]),
                                "y": int(attr[4])
                                }
                    elif cls.__name__ == "Square":
                        dictionary = {
                                "id": int(attr[0]),
                                "size": int(attr[1]),
                                "x": int(attr[2]),
                                "y": int(attr[3])
                                }
                    lst_obj = cls.create(**dictionary)
                    lst.append(lst_obj)
        except Exception as e:
            pass
        return lst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
        turtle.screensize(300,300)
        turtle.bgpic("h4.png")
        turtle.pensize(4)
        turtle.shape("arrow")
        colors = ["red", "purple", "blue"]

        turtle.color(random.choices(colors))
        for rect in list_rectangles:
            turtle.st()
            turtle.up()
            turtle.setposition(rect.x, rect.y)
            turtle.down()
            for i in range(2):
                turtle.speed(2)
                turtle.begin_fill()
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
                turtle.end_fill()
            turtle.ht()
            turtle.delay(15)

        turtle.color(random.choices(colors))
        for squ in list_squares:
            turtle.st()
            turtle.up()
            turtle.setposition(squ.x, squ.y)
            turtle.down()
            for i in range(2):
                turtle.speed(2)
                turtle.begin_fill()
                turtle.forward(squ.width)
                turtle.left(90)
                turtle.forward(squ.height)
                turtle.left(90)
                turtle.end_fill()
            turtle.ht()
            turtle.delay(15)

        
        turtle.color(random.choices(colors))
        turtle.st()
        turtle.up()
        turtle.setposition(0, -289)
        turtle.down()
        turtle.write("All Squares and Rectangles have been printed",
                    True, align="left", font=("Tahoma",8,"bold"))
        turtle.ht()

        turtle.exitonclick()
