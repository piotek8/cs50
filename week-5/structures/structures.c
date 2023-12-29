// Quick definition: A structure is a data type that allows you to group related data under a single name.
// This makes it easier to store and manipulate data,
// and it also helps to improve the readability and maintainability of your code.
// For example, you could put a person's name, age, and address in the same structure.

struct car
{
    int year;
    char model[10];
    char plate[7];
    int odometer;
    double engine_size;
};

// variable declaration
struct car mycar;

// field accessing
mycar.year = 2011;
strcpy(mycar.plate, "CS50");
mycar.odometer = 50505;



// variable declaration
struct car *mycar = malloc(sizeof(struct car));

//field accessing
(*mycar).year = 2011;
strcpy((*mycar)).plate, "CS50");
(*mycar).odometer = 50505;



// variable declaration
struct car *mycar = malloc(sizeof(struct car));

//field accessing
mycar->year = 2011;
strcpy(mycar->plate, "CS50");
mycar->odometer = 50505;
