#include <iostream>
#include <vector>

/*

	extract this class and add member functions for DFS and BFS
	to cut down on boilerplate dev time

	Make it really rock solid--don't give away internals you fool

*/

class Node{
	private:
		int id;
		bool visited;
		Node * pred;
		vector<Node> children;
	public:
		Node(int);

		void addChild(Node);
		void setPred(Node);
		void setVisited(bool);
		void reset(void);
		
		vector<Node> getChildren(void);
		Node * getPred(void);
		bool visited(void);
};

Node::Node(int i){
	id = i;
	visited = false;
	pred = NULL;
	children = vector<Node>();
}

void Node::addChild(Node& child){
	children.push_back(child);
}

void Node::setPred(Node& parent){
	pred = &parent;
}

void Node::setVisited(bool visit){
	visited = visit;
}

void Node::reset(){
	pred = NULL;
	visited = false;
}

vector<Node> Node::getChildren(){
	return children;
}

Node* Node::getPred(){
	return pred;
}

bool Node::visited(){
	return visited;
}

