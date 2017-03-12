/*

    Serialize / Deserialize Binary Tree
    "[1,2,3,null,null,4,5]"
        * basically an array representation as a string.
        * Each node has mathematical place.
        * Lay out array as complete binary tree of depth i. Kth node at depth i is at position 2^i + k. If no node, null
        * PROBLEM: VERY SPACE INEFFICIENT, exponential space complexity, most of which is likely empty nodes
        * Tree like 1-2-3-4-5-6-7-8-9-0 has only 10 nodes, but requires 512 array entries, most of which are NULL!
    "[1[2,3[4,5]]]"
        * recursive solution.
        * only make calls for given node when it is followed by brackets. We call add child on it.
        * terminate when we reach comma or closing bracket
        * edge cases:
            * no left node: just do [,right_node] --> instant comma lets us know.

*/

/**
 * Definition for a binary tree node.
 * 
 */

// function TreeNode(val) {
//       this.val = val;
//       this.left = this.right = null;
//  }

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    return '[' + serializeInner(root) + ']';
};

var serializeInner = function(node) {
    var s = '';
    if(node === null) return s;
    
    s += node.val;
    if(node.left !== null || node.right !== null){
        s += '[' + serializeInner(node.left) + ',' + serializeInner(node.right) + ']';
    }
    return s;
}

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    var root;
    if(data.length === 0 || data === '[]') return null;
    else{
        let parseResult = parseIntSubstring(data,1);
        root = new TreeNode(parseResult.val);
        if(data[parseResult.nextIndex] === '['){
            let deserializeResult = deserializeInner(data,parseResult.nextIndex + 1);
            root.left = deserializeResult.node;
            root.right = deserializeInner(data,deserializeResult.nextIndex).node;
        }
        return root;
    }
};

var parseIntSubstring = function(str,startIndex) {
    var i = startIndex, result = '';
    if(str[i] === '-'){
        result += str[i];
        i++;
    }
    while(isNumeric(str[i])) {
        result += str[i];
        i++;
    }
    return {val: parseInt(result),nextIndex: i};
};

var isNumeric = function(c) {
    return !isNaN(parseInt(c)) && isFinite(c);
}

var deserializeInner = function(str,startIndex) {
    var deserialized = {
        node: null,
        nextIndex: startIndex + 1
    };
    
    if(str[startIndex] === ',' || str[startIndex] === ']') return deserialized;
    else {
        let parseResult = parseIntSubstring(str,startIndex);
        deserialized.node = new TreeNode(parseResult.val);
        if(str[parseResult.nextIndex] === '['){
            let deserializeResult = deserializeInner(str,parseResult.nextIndex + 1);
            deserialized.node.left = deserializeResult.node;
            
            deserializeResult = deserializeInner(str,deserializeResult.nextIndex);
            deserialized.node.right = deserializeResult.node;
            deserialized.nextIndex = deserializeResult.nextIndex + 1;
        }else{
            deserialized.nextIndex = parseResult.nextIndex + 1;
        }
        return deserialized;
        // result.node = new TreeNode(parseInt())
    }
}

var testSerialize = function() {
    var tree;
    console.log(serialize(null));
    tree = new TreeNode(1);
    tree.left = new TreeNode(2);
    tree.right = new TreeNode(3);
    console.log(serialize(tree));
    tree.right.left = new TreeNode(4);
    tree.right.right = new TreeNode(5);
    // console.log(serialize(tree));
}

var testDeserialize = function() {
    assert(deserialize('') === null, 'TC0');
    assert(deserialize('[]') === null, 'TC1');
    
    var tree = new TreeNode(1);
    assert(equalsTree(deserialize('[1]'),tree),'TC2');
    
    tree.left = new TreeNode(2);
    tree.right = new TreeNode(3);
    assert(equalsTree(deserialize('[1[2,3]]'),tree),'TC3');
}

var equalsTree = function(t1,t2) {
    if(t1 === undefined || t2 === undefined) {
        return false;
    }
    else if(t1 === null && t2 === null) {
        return true;
    }else if(t1 !== null && t2 !== null) {
        if(t1.val === t2.val){
            return equalsTree(t1.left,t2.left) && equalsTree(t1.right,t2.right);
        }else {
            return false;
        }
    }else {
        return false;
    }
}

var assert = function(condition,msg) {
    if(!condition){
        console.log('FAILED ASSERTION ' + msg);
        throw Error('ASSERTION FAILED');
    }else{
        console.log(msg);   
    }
}

var testParseIntSubstring = function() {
    assert(parseIntSubstring('123bdjfd',0).val==123,'PIS0');
    assert(parseIntSubstring('123bdjfd',1).val==23,'PIS1');
    assert(parseIntSubstring('123bdj342fd',6).val==342,'PIS2');
}

var test = function(){
    testSerialize();
    testDeserialize();   
    testParseIntSubstring();
}

// test();

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
