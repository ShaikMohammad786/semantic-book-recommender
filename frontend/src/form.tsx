import axios from "axios";
import {useState} from "react";

type Book = {
    title :string;
    thumbnail:string;
    description:string;
}

export function Form(){

    const [query , setQuery] = useState("");
    const [category , setCategory] = useState("");
    const [emotion , setEmotion] = useState("");
    const [top_k , setTop_k] = useState(1);

    const [books , setBooks] = useState<Book[]>([]);


    const handleSubmit = async ( e: any) =>{
        e.preventDefault(); 
        const res = await axios.post("http://127.0.0.1:8000/recommendations", {
            query,
            category,
            emotion,
            top_k
        });
        

        setBooks(res.data.books)
        

       console.log(res);
    }

    return (

        <div>


            <form onSubmit={handleSubmit}>

               <textarea placeholder="Enter your query" value ={query} onChange={(e)=>setQuery(e.target.value)}/>

            <select  value={category}
        onChange={(e) => setCategory(e.target.value)}>
                <option value="">Select Category</option>
                <option value="Fiction">Fiction</option>
                <option value="Nonfiction">Nonfiction</option>
                <option value="Children's Fiction">Children's Fiction</option>
                <option value="Children's Nonfiction">Children's Nonfiction</option>

            </select>

            <select value={emotion}
        onChange={(e) => setEmotion(e.target.value)}> 
                <option value="">Select Emotion</option>
                <option value="admiration">Admiration</option>
                <option value="amusement">Amusement</option>
                <option value="anger">Anger</option>
                <option value="annoyance">Annoyance</option>
                <option value="approval">Approval</option>
                <option value="caring">Caring</option>
                <option value="confusion">Confusion</option>
                <option value="curiosity">Curiosity</option>
                <option value="desire">Desire</option>
                <option value="disappointment">Disappointment</option>
                <option value="disapproval">Disapproval</option>
                <option value="disgust">Disgust</option>
                <option value="embarrassment">Embarrassment</option>
                <option value="excitement">Excitement</option>
                <option value="fear">Fear</option>
                <option value="gratitude">Gratitude</option>
                <option value="grief">Grief</option>
                <option value="joy">Joy</option>
                <option value="love">Love</option>
                <option value="nervousness">Nervousness</option>
                <option value="neutral">Neutral</option>
                <option value="optimism">Optimism</option>
                <option value="pride">Pride</option>
                <option value="realization">Realization</option>
                <option value="relief">Relief</option>
                <option value="remorse">Remorse</option>
                <option value="sadness">Sadness</option>
                <option value="surprise">Surprise</option>
            </select>

            <input value={top_k}
        onChange={(e) => setTop_k(Number(e.target.value))}
                type="number"
                placeholder="No of retrievals"
             />

             <button type = "submit" >Semantic Recommendation</button>

            </form>



            <div>

                {books.map((book, index) => (
                    <div key={index}>

                        <h2>{book.title}</h2>

                        <img src={book.thumbnail} alt={book.title}/>

                        <p>{book.description}</p>

                    </div>
                ))}

            </div>




        </div>

        


    )




}
