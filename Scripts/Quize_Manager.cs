using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Quize_Manager : MonoBehaviour
{
    int Judge;
    // Start is called before the first frame update
    void Start()
    {
        Judge=-1;
    }

    int Judge_Answer(string choiced_ans,string ans){
        if(choiced_ans==ans){
            Judge=1;
            return Judge;
        }
        else{
            return Judge;
        }
    }
 
}
