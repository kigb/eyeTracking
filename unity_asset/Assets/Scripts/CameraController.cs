using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    //当player运动的时候，需要把camera跟着player一起运动
    //先获取当前camera的位置，然后加上player的位置，就可以实现camera跟着player一起运动
    public GameObject player;
    private Vector3 offset;
    // Start is called before the first frame update
    void Start()
    {
        offset = transform.position;//获取当前camera的位置
    }

    // Update is called once per frame
    void LateUpdate()
    {
        transform.position = offset + player.transform.position;//加上player的位置,player的初始位置要是0
    }
}
