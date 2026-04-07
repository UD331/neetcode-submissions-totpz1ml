class Node {
    public:
        int k; int v; Node* prev; Node* next;
        Node(int k, int v): k(k), v(v), prev(nullptr), next(nullptr){}
};

class LRUCache {
    private:
        int cap;
        unordered_map<int, Node*> cache;
        Node* right;
        Node* left;
        
        void remove(Node* node) {
            Node* p= node->prev;
            Node* n= node->next;
            p->next = n;
            n->prev = p;
        }
        void insert(Node* node) {
            Node* p= right->prev;
            p->next = node;
            node->prev = p;
            node->next = right;
            right->prev = node;
        }

public:
    LRUCache(int capacity) {
        cap = capacity;
        cache.clear();
        right = new Node(0, 0);
        left = new Node(0, 0);
        left->next = right;
        right->prev = left;
    }
    
    int get(int key) {
        if (cache.find(key) != cache.end()) {
            Node* n = cache[key];
            remove(n);
            insert(n);
            return n->v;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            remove(cache[key]);
        }
        Node* newNode = new Node(key, value);
        cache[key] = newNode;
        insert(newNode);

        if (cache.size() > cap) {
            Node* lru = left->next;
            remove(lru);
            cache.erase(lru->k);
            delete lru;
        }
    }
};
