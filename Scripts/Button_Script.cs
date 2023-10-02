using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using UnityEngine.SceneManagement;

public class Button_Script : MonoBehaviour
{
    string choiced_ans=None;
    string ans;
    public void OnClick_1(){
        Debug.Log("Clicked ○");
        choiced_ans="○";
    }

    public void OnClick_2(){
        Debug.Log("Clicked ✕");
        choiced_ans="✕";
        int Judge=Quize_Manager.Judge_Answer(choiced_ans,ans);
    }

    public void Scene_GameStart(){
        SceneManager.LoadScene("○✕quize");
    }
}
