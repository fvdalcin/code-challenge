package dalcin.bearch.mobilechallenge;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;

public class RepositoryListActivity extends Activity {

    private ListView mRepositoryListView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_repository_list);

        mRepositoryListView = (ListView) findViewById(R.id.repository_list);
        ArrayList<String> repositoryItems = new ArrayList<String>();
        repositoryItems.add("Item 1");
        repositoryItems.add("Item 2");
        repositoryItems.add("Item 3");
        repositoryItems.add("Item 4");

        ArrayAdapter adapter = new ArrayAdapter(this, android.R.layout.simple_list_item_1, repositoryItems);
        mRepositoryListView.setAdapter(adapter);
    }
}
