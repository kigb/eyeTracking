using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour
{
    
    public float speed;
    private int count;
    public Text countText;
    // Start is called before the first frame update
    void Start()
    {
        count = 0;
        setCountText();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void FixedUpdate()
    {
        float moveHorizontal = Input.GetAxis("Horizontal");//x轴
        float moveVertical = Input.GetAxis("Vertical");//z轴

        Vector3 movement = new Vector3(moveHorizontal, 0, moveVertical);
        GetComponent<Rigidbody>().AddForce(movement * speed * Time.deltaTime);
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("rotator"))
        {
            count++;
            other.gameObject.SetActive(false);
            Debug.Log("count: " + count);
            setCountText();
        }
    }
    void setCountText()
    {
        countText.text = "Count: " + count.ToString();
    }
}
