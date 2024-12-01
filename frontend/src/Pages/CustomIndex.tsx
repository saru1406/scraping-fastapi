import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

type Job = {
    id: number;
    title: string;
    show: string;
    price: string;
    tags: string;
    link: string;
    limit: string;
}

function CustomIndex() {
    const [jobs, setJobs] = useState<Job[]>([]);
    const [message, setMessage] = useState("");
    const [formData, setFormData] = useState({
        title: "",
        body: ""
    });

    useEffect(() => {
        const fetchJobs = async () => {
            const url = 'http://localhost:80/jobs';
            try {
                const response = await fetch(url, {
                    method: 'GET'
                });
                if (response.ok) {
                    const data = await response.json();
                    setJobs(data);
                } else {
                    console.error('Failed to fetch jobs:', response.statusText);
                }
            } catch (error) {
                console.error('Error fetching jobs:', error);
            }
        };

        fetchJobs();
    }, []);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log("送信されるデータ:", formData);
    
        try {
            const response = await fetch("http://localhost:80/qdrant", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });
    
            if (response.ok) {
                setMessage("データが正常に送信されました！");
                setFormData({ title: "", body: "" }); // フォームリセット
            } else {
                setMessage("データ送信に失敗しました。");
            }
        } catch (error) {
            console.error("送信中にエラーが発生しました:", error);
            setMessage("エラーが発生しました。");
        }
    };
    return (
        <div className="container">
            <section className="text-gray-600 body-font">
                <Link to="/" className="m-28 hover:text-gray-300 text-xl">戻る</Link>
                <div className="container px-5 py-24 mx-auto">
                    <div className="flex flex-col text-center w-full mb-20">
                        <h2 className="font-medium title-font tracking-widest text-gray-900 mb-4 text-center sm:text-left text-4xl ml-20">予定・TODO追加</h2>
                        <div className="flex justify-center items-center">
                            <form className="bg-white p-10 rounded w-2/3" onSubmit={handleSubmit}>
                                <div className="mb-5">
                                    <label className="block text-gray-700 text-sm font-bold mb-2">
                                        タイトル:
                                    </label>
                                    <input
                                        type="text"
                                        name="title"
                                        value={formData.title}
                                        onChange={handleChange}
                                        className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:bg-transparent focus:ring-2 focus:ring-indigo-200 focus:border-indigo-500 text-base outline-none text-gray-700 py-2 px-4 leading-8 transition-colors duration-200 ease-in-out"
                                    />
                                </div>
                                <div className="mb-5">
                                    <label className="block text-gray-700 text-sm font-bold mb-2">
                                        内容:
                                    </label>
                                    <textarea
                                        name="body"
                                        value={formData.body}
                                        onChange={handleChange}
                                        className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:bg-transparent focus:ring-2 focus:ring-indigo-200 focus:border-indigo-500 text-base outline-none text-gray-700 py-2 px-4 leading-8 transition-colors duration-200 ease-in-out"
                                    />
                                </div>
                                <button
                                    type="submit"
                                    className="w-full bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded"
                                >
                                    送信
                                </button>
                            </form>
                        </div>
                        <hr />
                        <h1 className="sm:text-4xl text-3xl font-medium title-font mb-2 text-gray-900 mt-10">登録データ一覧</h1>
                    </div>
                    <div className="lg:w-11/12 w-full mx-auto">
                        <table className="table-fixed w-full text-left whitespace-no-wrap">
                            <thead>
                                <tr>
                                    <th className="px-4 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100 rounded-tl rounded-bl w-1/4">タイトル</th>
                                    <th className="px-4 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100 w-1/2">内容</th>
                                </tr>
                            </thead>
                            <tbody>
                                {jobs.map(job => (
                                    <tr key={job.id} onClick={() => window.open(job.link, '_blank')} style={{ cursor: 'pointer' }}>
                                        <td className="px-4 py-3 border">{job.title}</td>
                                        <td className="px-4 py-3 border">{job.show}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>
        </div>

    )
}

export default CustomIndex;