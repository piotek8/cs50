
typedef struct _queue
{
    VALUE array[CAPACITY];
    int front;
    int size;

}
queue;


// Linked list-based implementation
typedef struct _queue
{
    VALUE val;
    struct _queue *prev;
    struct _queue *next;

}
queue;
